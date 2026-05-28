"""Commissions resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def create(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/commissions/records", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get(config: Dict[str, Any], commission_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/commissions/records/{commission_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_commissions(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None and v != ""}
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/records", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def approve(config: Dict[str, Any], commission_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/commissions/records/{commission_id}/approve",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def reject(
    config: Dict[str, Any],
    commission_id: str,
    reason: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/commissions/records/{commission_id}/reject",
        body={"reason": reason} if reason else None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def mark_paid(
    config: Dict[str, Any],
    commission_id: str,
    opts: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/commissions/records/{commission_id}/mark-paid",
        body=opts or {},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_rules(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/rules", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def create_rule(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/commissions/rules", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def update_rule(config: Dict[str, Any], rule_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PUT", f"/v1/commissions/rules/{rule_id}", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def delete_rule(config: Dict[str, Any], rule_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/commissions/rules/{rule_id}", **_opts_kw(config, **kwargs)
    )


def get_payout_summary(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/commissions/partners/{partner_id}/payout-summary",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_wallet_balance(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/commissions/partners/{partner_id}/wallet",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def request_payout(
    config: Dict[str, Any],
    partner_id: str,
    amount: float,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/commissions/partners/{partner_id}/payouts",
        body={"amount": amount},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_payout_history(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/commissions/partners/{partner_id}/payouts",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_summary(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/summary", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_by_partner(
    config: Dict[str, Any],
    partner_id: str,
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {"partnerId": partner_id, **(params or {})}
    query = {k: v for k, v in query.items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/records", query=query, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_total_owed(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/total-owed", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_total_paid(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/commissions/total-paid", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]
