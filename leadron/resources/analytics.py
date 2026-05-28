"""Analytics resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def get_overview(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/analytics/overview", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_lead_metrics(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/analytics/leads", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_commission_metrics(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/analytics/commissions",
        query=query or None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_partner_metrics(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/analytics/partners",
        query=query or None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_conversion_rate(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/analytics/conversion-rate",
        query=query or None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_sms_metrics(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/analytics/sms", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]
