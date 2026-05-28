# Leadron Python SDK

Official Python SDK for the [Leadron](https://leadron.io) API — lead management and partner commission platform.

## Install

```bash
pip install leadron
```

## Usage

```python
from leadron import Leadron

client = Leadron(
    api_key="your-api-key",
    base_url="https://api.leadron.io",  # optional, default production
)

# Auth
valid = client.auth.validate()
scopes = client.auth.get_scopes()

# Leads
lead = client.leads.create({
    "email": "jane@example.com",
    "firstName": "Jane",
    "lastName": "Doe",
})
listing = client.leads.list(params={"status": "qualified", "limit": 20})
for item in listing["auto_paginate"]:
    print(item["email"])

# Partners & commissions
partner = client.partners.get(partner_id)
client.commissions.approve(commission_id)

# Webhook signature verification (client-side)
is_valid = client.auth.verify_webhook_signature(raw_body, signature, secret)
event = client.webhooks.construct_event(raw_body, signature, secret)

# Optional: idempotency and request ID
client.leads.create(data, idempotency_key="unique-key-123", request_id="my-request-id")

# Rate limit (from last response)
remaining = client.get_rate_limit_status()
```

## API surface

- **auth** — validate, get_scopes, verify_webhook_signature
- **leads** — create, get, update, delete, list (with auto_paginate), assign, update_status, add_note, get_notes, get_timeline, mark_converted, bulk_create, bulk_assign, bulk_update_status, search, filter
- **partners** — create, get, update, list, deactivate, get_referral_tree, get_upline, get_referral_link, get_stats, get_leaderboard, get_top_performers, invite, resend_invite, get_onboarding_status, send_agreement, get_signed_documents, get_agreement_status
- **commissions** — create, get, list, approve, reject, mark_paid, get_rules, create_rule, update_rule, delete_rule, get_payout_summary, get_wallet_balance, request_payout, get_payout_history, get_summary, get_by_partner, get_total_owed, get_total_paid
- **sequences** — create, get, list, update, delete, activate, pause, enroll_lead, enroll_bulk, unenroll_lead, get_enrolled_leads, add_step, update_step, delete_step, reorder_steps
- **sms** — send, get_inbox, get_outbox, get_conversation, get_usage
- **phone_numbers** — search, list, get, release, assign_to_team, unassign_from_team, get_usage, get_10dlc_status
- **teams** — create, get, list, update, delete, add_member, remove_member, get_members, assign_lead, assign_phone_number, get_stats, get_leaderboard
- **documents** — templates (create, list, get, update, delete), send, send_to_partner, get, list, get_status, download, get_audit_trail, void, resend
- **webhooks** — create, list, get, update, delete, test, get_logs, retry, construct_event
- **analytics** — get_overview, get_lead_metrics, get_commission_metrics, get_partner_metrics, get_conversion_rate, get_sms_metrics
- **reports** — leads, commissions, partners, export
- **account** — get, update, get_branding, update_branding, api_keys (list, create, revoke), get_usage, get_plan, get_limits

## Webhook events

See [instructions.md](../instructions.md) for the full list of webhook event types. Verify payloads with `client.auth.verify_webhook_signature(payload, signature, secret)` before processing.

## API docs

Full API reference: [OpenAPI spec](../../documentation/api-docs/openapi.yaml) and [SDK-to-HTTP mapping](../api-mapping.md).
