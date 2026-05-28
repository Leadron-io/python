"""Partners resource."""

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
    res = http_module.request(config["api_key"], "POST", "/v1/partners", body=body, **_opts_kw(config, **kwargs))
    return res["data"]


def get(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "GET", f"/v1/partners/{partner_id}", **_opts_kw(config, **kwargs))
    return res["data"]


def update(config: Dict[str, Any], partner_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PUT", f"/v1/partners/{partner_id}", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_partners(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None and v != ""}
    res = http_module.request(
        config["api_key"], "GET", "/v1/partners", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def deactivate(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", f"/v1/partners/{partner_id}/deactivate", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_referral_tree(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/hierarchy", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_upline(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/hierarchy", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_referral_link(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/referral-link", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_stats(
    config: Dict[str, Any],
    partner_id: str,
    opts: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (opts or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/metrics", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_leaderboard(config: Dict[str, Any], opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (opts or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/partners/leaderboard", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_top_performers(config: Dict[str, Any], opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    query = {k: v for k, v in (opts or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/partners/leaderboard", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def invite(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "POST", "/v1/partners/invite", body=body, **_opts_kw(config, **kwargs))
    return res["data"]


def resend_invite(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", f"/v1/partners/{partner_id}/resend-invite", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_onboarding_status(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/onboarding", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def send_agreement(
    config: Dict[str, Any],
    partner_id: str,
    template_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/partners/{partner_id}/agreements/send",
        body={"templateId": template_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_signed_documents(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/documents/signed", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_agreement_status(config: Dict[str, Any], partner_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/partners/{partner_id}/agreement-status", **_opts_kw(config, **kwargs)
    )
    return res["data"]
