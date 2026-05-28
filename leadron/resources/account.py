"""Account resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def get(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "GET", "/v1/account", **_opts_kw(config, **kwargs))
    return res["data"]


def update(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PATCH", "/v1/account", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_branding(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/account/branding", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def update_branding(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PUT", "/v1/account/branding", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


# --- API Keys ---


def api_keys_list(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "GET", "/v1/api-keys", **_opts_kw(config, **kwargs))
    return res["data"]


def api_keys_create(config: Dict[str, Any], body: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/api-keys", body=body or {}, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def api_keys_revoke(config: Dict[str, Any], key_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/api-keys/{key_id}", **_opts_kw(config, **kwargs)
    )


def get_usage(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/account/usage", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_plan(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/account/plan", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_limits(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/account/limits", **_opts_kw(config, **kwargs)
    )
    return res["data"]
