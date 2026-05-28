"""Leadron API client."""

from typing import Any, Dict, Optional

from leadron import http as http_module
from leadron.resources import account as account_module
from leadron.resources import analytics as analytics_module
from leadron.resources import auth as auth_module
from leadron.resources import commissions as commissions_module
from leadron.resources import documents as documents_module
from leadron.resources import leads as leads_module
from leadron.resources import marketers as marketers_module
from leadron.resources import partners as partners_module
from leadron.resources import phone_numbers as phone_numbers_module
from leadron.resources import reports as reports_module
from leadron.resources import sequences as sequences_module
from leadron.resources import sms as sms_module
from leadron.resources import teams as teams_module
from leadron.resources import webhooks as webhooks_module


def _config(api_key: str, base_url: Optional[str] = None, max_retries: Optional[int] = None) -> Dict[str, Any]:
    out = {"api_key": api_key}
    if base_url is not None:
        out["base_url"] = base_url
    if max_retries is not None:
        out["max_retries"] = max_retries
    return out


class _Resource:
    """Base for resource namespaces that hold config and delegate to module functions."""

    def __init__(self, config: Dict[str, Any], module: Any):
        self._config = config
        self._module = module


class _Auth:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def validate(self, **kwargs: Any) -> Dict[str, Any]:
        return auth_module.validate(self._config, **kwargs)

    def get_scopes(self, **kwargs: Any) -> Dict[str, Any]:
        return auth_module.get_scopes(self._config, **kwargs)

    def verify_webhook_signature(self, payload: str, signature: str, secret: str) -> bool:
        return auth_module.verify_webhook_signature(payload, signature, secret)


class _Leads:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return leads_module.create(self._config, body, **kwargs)

    def get(self, lead_id: str, **kwargs: Any) -> Any:
        return leads_module.get(self._config, lead_id, **kwargs)

    def update(self, lead_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return leads_module.update(self._config, lead_id, body, **kwargs)

    def delete(self, lead_id: str, **kwargs: Any) -> None:
        return leads_module.delete(self._config, lead_id, **kwargs)

    def list(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        return leads_module.list_leads(self._config, params, **kwargs)

    def assign(self, lead_id: str, user_id: str, **kwargs: Any) -> Any:
        return leads_module.assign(self._config, lead_id, user_id, **kwargs)

    def update_status(self, lead_id: str, status: str, **kwargs: Any) -> Any:
        return leads_module.update_status(self._config, lead_id, status, **kwargs)

    def add_note(self, lead_id: str, content: str, **kwargs: Any) -> Any:
        return leads_module.add_note(self._config, lead_id, content, **kwargs)

    def get_notes(self, lead_id: str, **kwargs: Any) -> Any:
        return leads_module.get_notes(self._config, lead_id, **kwargs)

    def get_timeline(self, lead_id: str, **kwargs: Any) -> Any:
        return leads_module.get_timeline(self._config, lead_id, **kwargs)

    def mark_converted(
        self, lead_id: str, opts: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return leads_module.mark_converted(self._config, lead_id, opts, **kwargs)

    def bulk_create(self, leads: list, **kwargs: Any) -> Any:
        return leads_module.bulk_create(self._config, leads, **kwargs)

    def bulk_assign(self, lead_ids: list, partner_id: str, **kwargs: Any) -> Any:
        return leads_module.bulk_assign(self._config, lead_ids, partner_id, **kwargs)

    def bulk_update_status(self, lead_ids: list, status: str, **kwargs: Any) -> Any:
        return leads_module.bulk_update_status(self._config, lead_ids, status, **kwargs)

    def search(self, q: str, **kwargs: Any) -> Any:
        return leads_module.search(self._config, q, **kwargs)

    def filter(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return leads_module.filter(self._config, params, **kwargs)


class _Partners:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return partners_module.create(self._config, body, **kwargs)

    def get(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get(self._config, partner_id, **kwargs)

    def update(self, partner_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return partners_module.update(self._config, partner_id, body, **kwargs)

    def list(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return partners_module.list_partners(self._config, params, **kwargs)

    def deactivate(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.deactivate(self._config, partner_id, **kwargs)

    def get_referral_tree(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_referral_tree(self._config, partner_id, **kwargs)

    def get_upline(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_upline(self._config, partner_id, **kwargs)

    def get_referral_link(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_referral_link(self._config, partner_id, **kwargs)

    def get_stats(self, partner_id: str, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return partners_module.get_stats(self._config, partner_id, opts, **kwargs)

    def get_leaderboard(self, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return partners_module.get_leaderboard(self._config, opts, **kwargs)

    def get_top_performers(self, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return partners_module.get_top_performers(self._config, opts, **kwargs)

    def invite(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return partners_module.invite(self._config, body, **kwargs)

    def resend_invite(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.resend_invite(self._config, partner_id, **kwargs)

    def get_onboarding_status(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_onboarding_status(self._config, partner_id, **kwargs)

    def send_agreement(self, partner_id: str, template_id: str, **kwargs: Any) -> Any:
        return partners_module.send_agreement(self._config, partner_id, template_id, **kwargs)

    def get_signed_documents(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_signed_documents(self._config, partner_id, **kwargs)

    def get_agreement_status(self, partner_id: str, **kwargs: Any) -> Any:
        return partners_module.get_agreement_status(self._config, partner_id, **kwargs)


class _Marketers:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return marketers_module.create(self._config, body, **kwargs)

    def get(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get(self._config, partner_id, **kwargs)

    def update(self, partner_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return marketers_module.update(self._config, partner_id, body, **kwargs)

    def list(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return marketers_module.list_marketers(self._config, params, **kwargs)

    def deactivate(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.deactivate(self._config, partner_id, **kwargs)

    def get_referral_tree(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_referral_tree(self._config, partner_id, **kwargs)

    def get_upline(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_upline(self._config, partner_id, **kwargs)

    def get_referral_link(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_referral_link(self._config, partner_id, **kwargs)

    def get_stats(self, partner_id: str, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return marketers_module.get_stats(self._config, partner_id, opts, **kwargs)

    def get_leaderboard(self, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return marketers_module.get_leaderboard(self._config, opts, **kwargs)

    def get_top_performers(self, opts: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return marketers_module.get_top_performers(self._config, opts, **kwargs)

    def invite(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return marketers_module.invite(self._config, body, **kwargs)

    def resend_invite(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.resend_invite(self._config, partner_id, **kwargs)

    def get_onboarding_status(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_onboarding_status(self._config, partner_id, **kwargs)

    def send_agreement(self, partner_id: str, template_id: str, **kwargs: Any) -> Any:
        return marketers_module.send_agreement(self._config, partner_id, template_id, **kwargs)

    def get_signed_documents(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_signed_documents(self._config, partner_id, **kwargs)

    def get_agreement_status(self, partner_id: str, **kwargs: Any) -> Any:
        return marketers_module.get_agreement_status(self._config, partner_id, **kwargs)


class _Commissions:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return commissions_module.create(self._config, body, **kwargs)

    def get(self, commission_id: str, **kwargs: Any) -> Any:
        return commissions_module.get(self._config, commission_id, **kwargs)

    def list(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return commissions_module.list_commissions(self._config, params, **kwargs)

    def approve(self, commission_id: str, **kwargs: Any) -> Any:
        return commissions_module.approve(self._config, commission_id, **kwargs)

    def reject(self, commission_id: str, reason: Optional[str] = None, **kwargs: Any) -> Any:
        return commissions_module.reject(self._config, commission_id, reason, **kwargs)

    def mark_paid(
        self, commission_id: str, opts: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return commissions_module.mark_paid(self._config, commission_id, opts, **kwargs)

    def get_rules(self, **kwargs: Any) -> Any:
        return commissions_module.get_rules(self._config, **kwargs)

    def create_rule(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return commissions_module.create_rule(self._config, body, **kwargs)

    def update_rule(self, rule_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return commissions_module.update_rule(self._config, rule_id, body, **kwargs)

    def delete_rule(self, rule_id: str, **kwargs: Any) -> None:
        return commissions_module.delete_rule(self._config, rule_id, **kwargs)

    def get_payout_summary(self, partner_id: str, **kwargs: Any) -> Any:
        return commissions_module.get_payout_summary(self._config, partner_id, **kwargs)

    def get_wallet_balance(self, partner_id: str, **kwargs: Any) -> Any:
        return commissions_module.get_wallet_balance(self._config, partner_id, **kwargs)

    def request_payout(self, partner_id: str, amount: float, **kwargs: Any) -> Any:
        return commissions_module.request_payout(self._config, partner_id, amount, **kwargs)

    def get_payout_history(self, partner_id: str, **kwargs: Any) -> Any:
        return commissions_module.get_payout_history(self._config, partner_id, **kwargs)

    def get_summary(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return commissions_module.get_summary(self._config, params, **kwargs)

    def get_by_partner(
        self, partner_id: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return commissions_module.get_by_partner(self._config, partner_id, params, **kwargs)

    def get_total_owed(self, **kwargs: Any) -> Any:
        return commissions_module.get_total_owed(self._config, **kwargs)

    def get_total_paid(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return commissions_module.get_total_paid(self._config, params, **kwargs)


class _Sequences:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return sequences_module.create(self._config, body, **kwargs)

    def get(self, sequence_id: str, **kwargs: Any) -> Any:
        return sequences_module.get(self._config, sequence_id, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        return sequences_module.list_sequences(self._config, **kwargs)

    def update(self, sequence_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return sequences_module.update(self._config, sequence_id, body, **kwargs)

    def delete(self, sequence_id: str, **kwargs: Any) -> None:
        return sequences_module.delete(self._config, sequence_id, **kwargs)

    def activate(self, sequence_id: str, **kwargs: Any) -> Any:
        return sequences_module.activate(self._config, sequence_id, **kwargs)

    def pause(self, sequence_id: str, **kwargs: Any) -> Any:
        return sequences_module.pause(self._config, sequence_id, **kwargs)

    def enroll_lead(self, sequence_id: str, lead_id: str, **kwargs: Any) -> Any:
        return sequences_module.enroll_lead(self._config, sequence_id, lead_id, **kwargs)

    def enroll_bulk(self, sequence_id: str, lead_ids: list, **kwargs: Any) -> Any:
        return sequences_module.enroll_bulk(self._config, sequence_id, lead_ids, **kwargs)

    def unenroll_lead(self, sequence_id: str, lead_id: str, **kwargs: Any) -> Any:
        return sequences_module.unenroll_lead(self._config, sequence_id, lead_id, **kwargs)

    def get_enrolled_leads(self, sequence_id: str, **kwargs: Any) -> Any:
        return sequences_module.get_enrolled_leads(self._config, sequence_id, **kwargs)

    def add_step(self, sequence_id: str, step: Dict[str, Any], **kwargs: Any) -> Any:
        return sequences_module.add_step(self._config, sequence_id, step, **kwargs)

    def update_step(
        self, sequence_id: str, step_id: str, body: Dict[str, Any], **kwargs: Any
    ) -> Any:
        return sequences_module.update_step(self._config, sequence_id, step_id, body, **kwargs)

    def delete_step(self, sequence_id: str, step_id: str, **kwargs: Any) -> None:
        return sequences_module.delete_step(self._config, sequence_id, step_id, **kwargs)

    def reorder_steps(self, sequence_id: str, step_order: list, **kwargs: Any) -> Any:
        return sequences_module.reorder_steps(self._config, sequence_id, step_order, **kwargs)


class _Sms:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def send(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return sms_module.send(self._config, body, **kwargs)

    def get_inbox(
        self, phone_number_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        return sms_module.get_inbox(self._config, phone_number_id, **kwargs)

    def get_outbox(
        self, phone_number_id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        return sms_module.get_outbox(self._config, phone_number_id, **kwargs)

    def get_conversation(self, lead_id: str, **kwargs: Any) -> Any:
        return sms_module.get_conversation(self._config, lead_id, **kwargs)

    def get_usage(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return sms_module.get_usage(self._config, params, **kwargs)


class _PhoneNumbers:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def search(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return phone_numbers_module.search(self._config, params, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        return phone_numbers_module.list_phone_numbers(self._config, **kwargs)

    def get(self, number_id: str, **kwargs: Any) -> Any:
        return phone_numbers_module.get(self._config, number_id, **kwargs)

    def release(self, number_id: str, **kwargs: Any) -> None:
        return phone_numbers_module.release(self._config, number_id, **kwargs)

    def assign_to_team(self, number_id: str, team_id: str, **kwargs: Any) -> Any:
        return phone_numbers_module.assign_to_team(self._config, number_id, team_id, **kwargs)

    def unassign_from_team(self, number_id: str, team_id: str, **kwargs: Any) -> Any:
        return phone_numbers_module.unassign_from_team(self._config, number_id, team_id, **kwargs)

    def get_usage(
        self, number_id: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return phone_numbers_module.get_usage(self._config, number_id, params, **kwargs)

    def get_10dlc_status(self, number_id: str, **kwargs: Any) -> Any:
        return phone_numbers_module.get_10dlc_status(self._config, number_id, **kwargs)


class _Teams:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return teams_module.create(self._config, body, **kwargs)

    def get(self, team_id: str, **kwargs: Any) -> Any:
        return teams_module.get(self._config, team_id, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        return teams_module.list_teams(self._config, **kwargs)

    def update(self, team_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return teams_module.update(self._config, team_id, body, **kwargs)

    def delete(self, team_id: str, **kwargs: Any) -> None:
        return teams_module.delete(self._config, team_id, **kwargs)

    def add_member(self, team_id: str, user_id: str, **kwargs: Any) -> Any:
        return teams_module.add_member(self._config, team_id, user_id, **kwargs)

    def remove_member(self, team_id: str, user_id: str, **kwargs: Any) -> None:
        return teams_module.remove_member(self._config, team_id, user_id, **kwargs)

    def get_members(self, team_id: str, **kwargs: Any) -> Any:
        return teams_module.get_members(self._config, team_id, **kwargs)

    def assign_lead(self, team_id: str, lead_id: str, **kwargs: Any) -> Any:
        return teams_module.assign_lead(self._config, team_id, lead_id, **kwargs)

    def assign_phone_number(self, team_id: str, number_id: str, **kwargs: Any) -> Any:
        return teams_module.assign_phone_number(self._config, team_id, number_id, **kwargs)

    def get_stats(
        self, team_id: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return teams_module.get_stats(self._config, team_id, params, **kwargs)

    def get_leaderboard(self, **kwargs: Any) -> Any:
        return teams_module.get_leaderboard(self._config, **kwargs)


class _DocumentsTemplates:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return documents_module.templates_create(self._config, body, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        return documents_module.templates_list(self._config, **kwargs)

    def get(self, template_id: str, **kwargs: Any) -> Any:
        return documents_module.templates_get(self._config, template_id, **kwargs)

    def update(self, template_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return documents_module.templates_update(self._config, template_id, body, **kwargs)

    def delete(self, template_id: str, **kwargs: Any) -> None:
        return documents_module.templates_delete(self._config, template_id, **kwargs)


class _Documents:
    def __init__(self, config: Dict[str, Any]):
        self._config = config
        self._templates = _DocumentsTemplates(config)

    @property
    def templates(self) -> _DocumentsTemplates:
        return self._templates

    def send(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return documents_module.send(self._config, body, **kwargs)

    def send_to_partner(
        self, template_id: str, partner_id: str, **kwargs: Any
    ) -> Any:
        return documents_module.send_to_partner(self._config, template_id, partner_id, **kwargs)

    def get(self, document_id: str, **kwargs: Any) -> Any:
        return documents_module.get(self._config, document_id, **kwargs)

    def list(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return documents_module.list_documents(self._config, params, **kwargs)

    def get_status(self, document_id: str, **kwargs: Any) -> Any:
        return documents_module.get_status(self._config, document_id, **kwargs)

    def download(self, document_id: str, **kwargs: Any) -> Any:
        return documents_module.download(self._config, document_id, **kwargs)

    def get_audit_trail(self, document_id: str, **kwargs: Any) -> Any:
        return documents_module.get_audit_trail(self._config, document_id, **kwargs)

    def void(
        self, document_id: str, reason: Optional[str] = None, **kwargs: Any
    ) -> Any:
        return documents_module.void(self._config, document_id, reason, **kwargs)

    def resend(self, document_id: str, **kwargs: Any) -> Any:
        return documents_module.resend(self._config, document_id, **kwargs)


class _Webhooks:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def create(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return webhooks_module.create(self._config, body, **kwargs)

    def list(self, **kwargs: Any) -> Any:
        return webhooks_module.list_webhooks(self._config, **kwargs)

    def get(self, webhook_id: str, **kwargs: Any) -> Any:
        return webhooks_module.get(self._config, webhook_id, **kwargs)

    def update(self, webhook_id: str, body: Dict[str, Any], **kwargs: Any) -> Any:
        return webhooks_module.update(self._config, webhook_id, body, **kwargs)

    def delete(self, webhook_id: str, **kwargs: Any) -> None:
        return webhooks_module.delete(self._config, webhook_id, **kwargs)

    def test(self, webhook_id: str, **kwargs: Any) -> Any:
        return webhooks_module.test(self._config, webhook_id, **kwargs)

    def get_logs(self, webhook_id: str, **kwargs: Any) -> Any:
        return webhooks_module.get_logs(self._config, webhook_id, **kwargs)

    def retry(self, webhook_id: str, log_id: str, **kwargs: Any) -> Any:
        return webhooks_module.retry(self._config, webhook_id, log_id, **kwargs)

    @staticmethod
    def construct_event(raw_body: str, signature: str, secret: str) -> Any:
        return webhooks_module.construct_event(raw_body, signature, secret)


class _Analytics:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def get_overview(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return analytics_module.get_overview(self._config, params, **kwargs)

    def get_lead_metrics(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return analytics_module.get_lead_metrics(self._config, params, **kwargs)

    def get_commission_metrics(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return analytics_module.get_commission_metrics(self._config, params, **kwargs)

    def get_partner_metrics(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return analytics_module.get_partner_metrics(self._config, params, **kwargs)

    def get_conversion_rate(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return analytics_module.get_conversion_rate(self._config, params, **kwargs)

    def get_sms_metrics(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return analytics_module.get_sms_metrics(self._config, params, **kwargs)


class _Reports:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def leads(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return reports_module.leads(self._config, params, **kwargs)

    def commissions(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return reports_module.commissions(self._config, params, **kwargs)

    def partners(
        self, params: Optional[Dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        return reports_module.partners(self._config, params, **kwargs)

    def export(self, report_config: Dict[str, Any], **kwargs: Any) -> Any:
        return reports_module.export(self._config, report_config, **kwargs)


class _AccountApiKeys:
    def __init__(self, config: Dict[str, Any]):
        self._config = config

    def list(self, **kwargs: Any) -> Any:
        return account_module.api_keys_list(self._config, **kwargs)

    def create(self, body: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return account_module.api_keys_create(self._config, body, **kwargs)

    def revoke(self, key_id: str, **kwargs: Any) -> None:
        return account_module.api_keys_revoke(self._config, key_id, **kwargs)


class _Account:
    def __init__(self, config: Dict[str, Any]):
        self._config = config
        self._api_keys = _AccountApiKeys(config)

    @property
    def api_keys(self) -> _AccountApiKeys:
        return self._api_keys

    def get(self, **kwargs: Any) -> Any:
        return account_module.get(self._config, **kwargs)

    def update(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return account_module.update(self._config, body, **kwargs)

    def get_branding(self, **kwargs: Any) -> Any:
        return account_module.get_branding(self._config, **kwargs)

    def update_branding(self, body: Dict[str, Any], **kwargs: Any) -> Any:
        return account_module.update_branding(self._config, body, **kwargs)

    def get_usage(self, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        return account_module.get_usage(self._config, params, **kwargs)

    def get_plan(self, **kwargs: Any) -> Any:
        return account_module.get_plan(self._config, **kwargs)

    def get_limits(self, **kwargs: Any) -> Any:
        return account_module.get_limits(self._config, **kwargs)


class Leadron:
    """Leadron API client. All resources are namespaced under the client."""

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        max_retries: Optional[int] = None,
    ):
        self._rate_limit_ref: Dict[str, Optional[int]] = {"current": None}
        self._config = _config(api_key, base_url, max_retries)
        self._config["rate_limit_ref"] = self._rate_limit_ref
        self._auth = _Auth(self._config)
        self._leads = _Leads(self._config)
        self._partners = _Partners(self._config)
        self._marketers = _Marketers(self._config)
        self._commissions = _Commissions(self._config)
        self._sequences = _Sequences(self._config)
        self._sms = _Sms(self._config)
        self._phone_numbers = _PhoneNumbers(self._config)
        self._teams = _Teams(self._config)
        self._documents = _Documents(self._config)
        self._webhooks = _Webhooks(self._config)
        self._analytics = _Analytics(self._config)
        self._reports = _Reports(self._config)
        self._account = _Account(self._config)

    @property
    def auth(self) -> _Auth:
        return self._auth

    @property
    def leads(self) -> _Leads:
        return self._leads

    @property
    def partners(self) -> _Partners:
        return self._partners

    @property
    def marketers(self) -> _Marketers:
        return self._marketers

    @property
    def commissions(self) -> _Commissions:
        return self._commissions

    @property
    def sequences(self) -> _Sequences:
        return self._sequences

    @property
    def sms(self) -> _Sms:
        return self._sms

    @property
    def phone_numbers(self) -> _PhoneNumbers:
        return self._phone_numbers

    @property
    def teams(self) -> _Teams:
        return self._teams

    @property
    def documents(self) -> _Documents:
        return self._documents

    @property
    def webhooks(self) -> _Webhooks:
        return self._webhooks

    @property
    def analytics(self) -> _Analytics:
        return self._analytics

    @property
    def reports(self) -> _Reports:
        return self._reports

    @property
    def account(self) -> _Account:
        return self._account

    def get_rate_limit_status(self) -> Optional[int]:
        """Remaining requests in the current rate limit window (from last response)."""
        return self._rate_limit_ref.get("current")
