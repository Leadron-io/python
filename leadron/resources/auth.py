"""Auth resource."""

import hmac
import hashlib
from typing import Any, Dict

from leadron import http as http_module


def validate(
    config: Dict[str, Any],
    **kwargs: Any,
) -> Dict[str, Any]:
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/api-keys/validate",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return {"valid": res["data"].get("valid", True)}


def get_scopes(
    config: Dict[str, Any],
    **kwargs: Any,
) -> Dict[str, Any]:
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/api-keys/scopes",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return {"scopes": res["data"].get("scopes", [])}


def verify_webhook_signature(payload: str, signature: str, secret: str) -> bool:
    expected = hmac.new(
        secret.encode("utf-8"),
        payload.encode("utf-8") if isinstance(payload, str) else payload,
        hashlib.sha256,
    ).hexdigest()
    return hmac.compare_digest(expected, signature) or hmac.compare_digest(f"sha256={expected}", signature)
