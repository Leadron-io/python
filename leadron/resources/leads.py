"""Leads resource."""

from typing import Any, Dict, Iterator, List, Optional

from leadron import http as http_module


def _build_query(params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if not params:
        return {}
    q = {}
    for k in ("page", "limit", "status", "assigned_to", "source", "sort", "order", "from", "to"):
        v = params.get(k) if k in params else params.get(k.replace("_", ""))
        if v is not None and v != "":
            q[k] = v
    return q


def create(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/leads",
        base_url=config.get("base_url"),
        body=body,
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def get(config: Dict[str, Any], lead_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/leads/{lead_id}",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def update(config: Dict[str, Any], lead_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "PUT",
        f"/v1/leads/{lead_id}",
        base_url=config.get("base_url"),
        body=body,
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def delete(config: Dict[str, Any], lead_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"],
        "DELETE",
        f"/v1/leads/{lead_id}",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        **kwargs,
    )


def list_leads(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Dict[str, Any]:
    query = _build_query(params)
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/leads",
        base_url=config.get("base_url"),
        query=query or None,
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    data = res["data"] if isinstance(res["data"], list) else []
    pagination = res.get("pagination")

    def auto_paginate() -> Iterator[Any]:
        for item in data:
            yield item
        page = (params or {}).get("page", 1)
        limit = (params or {}).get("limit", 20)
        while pagination and pagination.get("hasNext"):
            page += 1
            next_params = dict(params or {}, page=page, limit=limit)
            next_res = list_leads(config, next_params, **kwargs)
            for item in next_res["data"]:
                yield item
            pagination = next_res.get("pagination")

    return {"data": data, "pagination": pagination, "auto_paginate": auto_paginate()}


def assign(
    config: Dict[str, Any],
    lead_id: str,
    user_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/leads/{lead_id}/assign",
        base_url=config.get("base_url"),
        body={"userId": user_id},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def update_status(
    config: Dict[str, Any],
    lead_id: str,
    status: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "PUT",
        f"/v1/leads/{lead_id}/status",
        base_url=config.get("base_url"),
        body={"status": status},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def add_note(
    config: Dict[str, Any],
    lead_id: str,
    content: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/leads/{lead_id}/notes",
        base_url=config.get("base_url"),
        body={"content": content},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def get_notes(config: Dict[str, Any], lead_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/leads/{lead_id}/notes",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def get_timeline(config: Dict[str, Any], lead_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        f"/v1/leads/{lead_id}/timeline",
        base_url=config.get("base_url"),
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def mark_converted(
    config: Dict[str, Any],
    lead_id: str,
    opts: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/leads/{lead_id}/convert",
        base_url=config.get("base_url"),
        body=opts or {},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def bulk_create(
    config: Dict[str, Any],
    leads: List[Dict[str, Any]],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/leads/bulk",
        base_url=config.get("base_url"),
        body={"leads": leads},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def bulk_assign(
    config: Dict[str, Any],
    lead_ids: List[str],
    partner_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/leads/bulk/assign",
        base_url=config.get("base_url"),
        body={"leadIds": lead_ids, "partnerId": partner_id},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def bulk_update_status(
    config: Dict[str, Any],
    lead_ids: List[str],
    status: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/leads/bulk/status",
        base_url=config.get("base_url"),
        body={"leadIds": lead_ids, "status": status},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def search(config: Dict[str, Any], q: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/search/leads",
        base_url=config.get("base_url"),
        query={"q": q},
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]


def filter(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = _build_query(params)
    res = http_module.request(
        config["api_key"],
        "GET",
        "/v1/leads",
        base_url=config.get("base_url"),
        query=query or None,
        max_retries=config.get("max_retries"),
        rate_limit_ref=config.get("rate_limit_ref"),
        **kwargs,
    )
    return res["data"]
