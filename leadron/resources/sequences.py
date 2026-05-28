"""Sequences resource."""

from typing import Any, Dict, List, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


def create(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "POST", "/v1/sequences", body=body, **_opts_kw(config, **kwargs))
    return res["data"]


def get(config: Dict[str, Any], sequence_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/sequences/{sequence_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_sequences(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(config["api_key"], "GET", "/v1/sequences", **_opts_kw(config, **kwargs))
    return res["data"]


def update(config: Dict[str, Any], sequence_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "PUT", f"/v1/sequences/{sequence_id}", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def delete(config: Dict[str, Any], sequence_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/sequences/{sequence_id}", **_opts_kw(config, **kwargs)
    )


def activate(config: Dict[str, Any], sequence_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", f"/v1/sequences/{sequence_id}/activate", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def pause(config: Dict[str, Any], sequence_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", f"/v1/sequences/{sequence_id}/pause", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def enroll_lead(
    config: Dict[str, Any],
    sequence_id: str,
    lead_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/sequences/{sequence_id}/enroll",
        body={"leadId": lead_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def enroll_bulk(
    config: Dict[str, Any],
    sequence_id: str,
    lead_ids: List[str],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/sequences/{sequence_id}/enroll/bulk",
        body={"leadIds": lead_ids},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def unenroll_lead(
    config: Dict[str, Any],
    sequence_id: str,
    lead_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/sequences/{sequence_id}/unenroll/{lead_id}",
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get_enrolled_leads(config: Dict[str, Any], sequence_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/sequences/{sequence_id}/enrolled", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def add_step(
    config: Dict[str, Any],
    sequence_id: str,
    step: Dict[str, Any],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/sequences/{sequence_id}/steps",
        body=step,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def update_step(
    config: Dict[str, Any],
    sequence_id: str,
    step_id: str,
    body: Dict[str, Any],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "PUT",
        f"/v1/sequences/{sequence_id}/steps/{step_id}",
        body=body,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def delete_step(config: Dict[str, Any], sequence_id: str, step_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"],
        "DELETE",
        f"/v1/sequences/{sequence_id}/steps/{step_id}",
        **_opts_kw(config, **kwargs),
    )


def reorder_steps(
    config: Dict[str, Any],
    sequence_id: str,
    step_order: List[str],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/sequences/{sequence_id}/steps/reorder",
        body={"stepOrder": step_order},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]
