"""Webhooks resource."""

import json
from typing import Any, Dict

from leadron import http as http_module
from leadron.resources import auth as auth_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def create(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/integrations/webhooks", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_webhooks(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/integrations/webhooks", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get(config: Dict[str, Any], webhook_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/integrations/webhooks/{webhook_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def update(config: Dict[str, Any], webhook_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "PUT",
        f"/v1/integrations/webhooks/{webhook_id}",
        body=body,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def delete(config: Dict[str, Any], webhook_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/integrations/webhooks/{webhook_id}", **_opts_kw(config, **kwargs)
    )


def test(config: Dict[str, Any], webhook_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/integrations/webhooks/{webhook_id}/test",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_logs(config: Dict[str, Any], webhook_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/integrations/webhooks/{webhook_id}/logs", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def retry(
    config: Dict[str, Any],
    webhook_id: str,
    log_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/integrations/webhooks/{webhook_id}/retry",
        body={"logId": log_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def construct_event(raw_body: str, signature: str, secret: str) -> Any:
    if not auth_module.verify_webhook_signature(raw_body, signature, secret):
        raise ValueError("Webhook signature verification failed")
    try:
        return json.loads(raw_body)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON in webhook payload") from e
