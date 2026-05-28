"""Reports resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def leads(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/reports/leads", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def commissions(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/reports/commissions", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def partners(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/reports/partners", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def export(config: Dict[str, Any], report_config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/reports/export", body=report_config, **_opts_kw(config, **kwargs)
    )
    return res["data"]
