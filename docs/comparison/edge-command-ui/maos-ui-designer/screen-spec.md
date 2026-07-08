# MAOS UI Designer Screen Spec

## Screen 1: Command Center Overview

Primary components:

- CommandCenterShell: role-aware navigation, environment switcher, global search, command safety banner, and notification center.
- FleetPostureSummary: active missions, degraded edge nodes, critical alerts, pending approvals, failed receipts, and stale telemetry.
- NodeHealthPanel: edge node connectivity, workload, local autonomy mode, command queue depth, last sync, and disconnected state.
- MissionTable: typed columns, stable `rowKey`, severity tags, command receipt health, owner, filters, sorting, selection, and bulk acknowledgement.
- AgentDecisionSummary: latest agent decision run, confidence, blocked constraints, evidence count, and audit status.

Expected states:

- loading skeleton, empty mission queue, error retry, partial data, stale data, disconnected node, permission-limited action, selected row, focus state, failed receipt.

## Screen 2: Alert Triage

Primary components:

- AlertTriageQueue: critical, warning, stale, disconnected, and acknowledged filters.
- AlertTimeline: alert source, severity, evidence, AI recommendation, acknowledgement, escalation, linked mission, and recovery notes.
- EvidenceViewer: telemetry, logs, image snapshot, command receipt, operator note, and audit trace.
- CommandDraftPanel: turns AI recommendation into a reviewable command draft without dispatching directly.

Expected actions:

- acknowledge, escalate, assign owner, open evidence, create command draft, export audit package.

## Screen 3: Command Approval Drawer

Primary components:

- CommandApprovalDrawer: target preview, command payload, policy checks, timeout, impact summary, and receipt status.
- PermissionGate: role gate with disabled reason, escalation path, and audit explanation.
- ApprovalTimeline: requester, approver, policy reason, expiry, receipt pending, failed receipt, retry eligibility, and audit replay.
- DestructiveConfirmation: names target, command, impact, timeout, and two-person approval requirement.

Expected states:

- permission-limited, destructive confirmation, two-person approval, command pending, receipt pending, timeout, failed, retry, success, audit replay.

## Responsive QA

- Desktop: 1440px command center with rail, posture summary, mission table, topology/health panel, and approval drawer.
- Tablet: secondary panels collapse into tabs.
- Mobile: alert handoff and approval review are readable; high-risk command authoring is disabled unless policy allows.

## Implementation Guardrails

- Ant Design is acceptable because the surface is Web B2B/admin and data dense.
- Use ConfigProvider theme tokens and domain wrappers to keep the UI agent-maintainable.
- Use StyleX for app-owned layout tokens, not arbitrary inline styles.
- Use typed chart adapters for ECharts or AntV.
- Add stable `data-testid` and `data-eval-*` attributes for screenshot and evaluator checks.
