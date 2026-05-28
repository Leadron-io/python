"""SMS resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def send(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    b = dict(body)
    if "message" in b and "body" not in b:
        b["body"] = b["message"]
    res = http_module.request(
        config["api_key"], "POST", "/v1/communications/send/sms", body=b, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_inbox(
    config: Dict[str, Any],
    phone_number_id: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    query = {"phoneNumberId": phone_number_id} if phone_number_id else None
    res = http_module.request(
        config["api_key"], "GET", "/v1/communications/inbox", query=query, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_outbox(
    config: Dict[str, Any],
    phone_number_id: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    query = {"phoneNumberId": phone_number_id} if phone_number_id else None
    res = http_module.request(
        config["api_key"], "GET", "/v1/communications/outbox", query=query, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_conversation(config: Dict[str, Any], lead_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/communications/conversations/{lead_id}",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_usage(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/communications/usage", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]
