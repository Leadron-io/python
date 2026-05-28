"""Documents resource."""

from typing import Any, Dict, Optional

from leadron import http as http_module


def _opts_kw(config: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
    return {
        "base_url": config.get("base_url"),
        "max_retries": config.get("max_retries"),
        "rate_limit_ref": config.get("rate_limit_ref"),
        **kwargs,
    }


# --- Templates ---


def templates_create(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/documents/templates", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def templates_list(config: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", "/v1/documents/templates", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def templates_get(config: Dict[str, Any], template_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/documents/templates/{template_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def templates_update(
    config: Dict[str, Any],
    template_id: str,
    body: Dict[str, Any],
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "PUT",
        f"/v1/documents/templates/{template_id}",
        body=body,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def templates_delete(config: Dict[str, Any], template_id: str, **kwargs: Any) -> None:
    http_module.request(
        config["api_key"], "DELETE", f"/v1/documents/templates/{template_id}", **_opts_kw(config, **kwargs)
    )


# --- Documents ---


def send(config: Dict[str, Any], body: Dict[str, Any], **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", "/v1/documents/send", body=body, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def send_to_partner(
    config: Dict[str, Any],
    template_id: str,
    partner_id: str,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        "/v1/documents/send-to-partner",
        body={"templateId": template_id, "partnerId": partner_id},
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def get(config: Dict[str, Any], document_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/documents/{document_id}", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def list_documents(
    config: Dict[str, Any],
    params: Optional[Dict[str, Any]] = None,
    **kwargs: Any,
) -> Any:
    query = {k: v for k, v in (params or {}).items() if v is not None}
    res = http_module.request(
        config["api_key"], "GET", "/v1/documents", query=query or None, **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_status(config: Dict[str, Any], document_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/documents/{document_id}/status", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def download(config: Dict[str, Any], document_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/documents/{document_id}/download", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def get_audit_trail(config: Dict[str, Any], document_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "GET", f"/v1/documents/{document_id}/audit-trail", **_opts_kw(config, **kwargs)
    )
    return res["data"]


def void(
    config: Dict[str, Any],
    document_id: str,
    reason: Optional[str] = None,
    **kwargs: Any,
) -> Any:
    res = http_module.request(
        config["api_key"],
        "POST",
        f"/v1/documents/{document_id}/void",
        body={"reason": reason} if reason else None,
        **_opts_kw(config, **kwargs),
    )
    return res["data"]


def resend(config: Dict[str, Any], document_id: str, **kwargs: Any) -> Any:
    res = http_module.request(
        config["api_key"], "POST", f"/v1/documents/{document_id}/resend", **_opts_kw(config, **kwargs)
    )
    return res["data"]
