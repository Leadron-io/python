"""Teams resource."""

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
    res = http_module.request(config["api_key"], "POST", "/v1/teams", body=body, **_opts_kw(config, **kwargs))
    return res["data"]


def get(config: Dict[str, Any], team_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/teams/{team_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_teams(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "GET", "/v1/teams", **_opts_kw(config, **kwargs))
    return res["data"]


def update(config: Dict[str, Any], team_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PUT", f"/v1/teams/{team_id}", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def delete(config: Dict[str, Any], team_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/teams/{team_id}", **_opts_kw(config, **kwargs)
    )


def add_member(
    config: Dict[str, Any],
    team_id: str,
    user_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/teams/{team_id}/members",
        body={"userId": user_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def remove_member(config: Dict[str, Any], team_id: str, user_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"],
        "DELETE",
        f"/v1/teams/{team_id}/members/{user_id}",
        **_opts_kw(config, **kwargs),
    )


def get_members(config: Dict[str, Any], team_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/teams/{team_id}/members", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def assign_lead(
    config: Dict[str, Any],
    team_id: str,
    lead_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/teams/{team_id}/assign/lead",
        body={"leadId": lead_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def assign_phone_number(
    config: Dict[str, Any],
    team_id: str,
    number_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/teams/{team_id}/assign/phone-number",
        body={"numberId": number_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_stats(
    config: Dict[str, Any],
    team_id: str,
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/teams/{team_id}/stats",
        query=query or None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_leaderboard(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/teams/leaderboard", **_opts_kw(config, **kwargs)
    )
    return res["data"]
