"""HTTP client with retry, API key auth, and optional idempotency/request ID."""

import time
from typing import Any, Dict, Optional

import requests

from leadron.exceptions import (
    LeadronAuthError,
    LeadronError,
    LeadronRateLimitError,
    LeadronValidationError,
)

DEFAULT_BASE_URL = "https://api.leadron.io"
DEFAULT_RETRIES = 3
RETRY_DELAY_SEC = 1


def _is_retryable(status_code: int) -> bool:
    return status_code == 429 or (500 <= status_code < 600)


def request(
    api_key: str,
    method: str,
    path: str,
    base_url: str = DEFAULT_BASE_URL,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None,
    idempotency_key: Optional[str] = None,
    max_retries: int = DEFAULT_RETRIES,
    rate_limit_ref: Optional[Dict[str, Optional[int]]] = None,
) -> Dict[str, Any]:
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    if request_id:
        headers["X-Request-Id"] = request_id
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    last_error = None
    for attempt in range(max_retries + 1):
        try:
            resp = requests.request(
                method,
                url,
                params=query,
                json=body,
                headers=headers,
                timeout=30,
            )

            rate_limit_remaining = None
            if "X-RateLimit-Remaining" in resp.headers:
                try:
                    rate_limit_remaining = int(resp.headers["X-RateLimit-Remaining"])
                except ValueError:
                    pass
            if rate_limit_ref is not None and rate_limit_remaining is not None:
                rate_limit_ref["current"] = rate_limit_remaining

            if resp.ok:
                data = resp.json() if resp.text else {}
                return {
                    "data": data.get("data", data),
                    "pagination": data.get("pagination"),
                    "rate_limit_remaining": rate_limit_remaining,
                }

            message = (resp.json() or {}).get("message", resp.reason or f"HTTP {resp.status_code}")
            status_code = resp.status_code
            try:
                response_body = resp.json()
            except Exception:
                response_body = resp.text

            if status_code == 401:
                raise LeadronAuthError(message, status_code, response_body)
            if status_code == 422:
                raise LeadronValidationError(message, status_code, response_body)
            if status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", RETRY_DELAY_SEC))
                if attempt < max_retries:
                    time.sleep(retry_after)
                    continue
                raise LeadronRateLimitError(message, retry_after, status_code, response_body)
            if _is_retryable(status_code) and attempt < max_retries:
                last_error = LeadronError(message, status_code, response_body)
                time.sleep(RETRY_DELAY_SEC * (attempt + 1))
                continue
            raise LeadronError(message, status_code, response_body)
        except (LeadronAuthError, LeadronValidationError, LeadronRateLimitError):
            raise
        except requests.RequestException as e:
            last_error = LeadronError(str(e), None, None)
            if attempt < max_retries:
                time.sleep(RETRY_DELAY_SEC * (attempt + 1))
                continue
            raise last_error
    raise last_error or LeadronError("Request failed")
