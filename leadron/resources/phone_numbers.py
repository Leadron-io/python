"""Phone numbers resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def search(config: Dict[str, Any], params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/phone-numbers",
        body=params or {},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def list_phone_numbers(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/phone-numbers", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get(config: Dict[str, Any], number_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/phone-numbers/{number_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def release(config: Dict[str, Any], number_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/phone-numbers/{number_id}", **_opts_kw(config, **kwargs)
    )


def assign_to_team(
    config: Dict[str, Any],
    number_id: str,
    team_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/phone-numbers/{number_id}/assign-team",
        body={"teamId": team_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def unassign_from_team(
    config: Dict[str, Any],
    number_id: str,
    team_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/phone-numbers/{number_id}/unassign-team",
        body={"teamId": team_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_usage(
    config: Dict[str, Any],
    number_id: str,
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/phone-numbers/{number_id}/usage",
        query=query or None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_10dlc_status(config: Dict[str, Any], number_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/phone-numbers/{number_id}/10dlc-status",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]
