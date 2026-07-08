# MAOS UI Designer Screen Spec

## Screen: Command Center Workbench

Primary model: selected mission `M-482`.

The screen is a selected-object workbench. The mission queue is the primary area, and every secondary module references the selected mission instead of acting as a standalone dashboard tile.

## Layout Formation Contract

- Layout formation: Workbench.
- Primary object: selected mission `M-482`.
- Primary region: mission queue and edge-node health.
- Secondary region: selected mission context, alert timeline, evidence, command approval, and receipt recovery.
- Responsive collapse: desktop two-column workbench, tablet stacked workbench, mobile context-first with table-internal scroll.
- Rejected formations: dashboard + drilldown hides the selected mission; wizard / stepper is too linear for live triage; canvas + inspector is not appropriate for this table-first approval workflow.

## Components

- CommandCenterShell: role-aware navigation, global search, command safety banner, and responsive rail behavior.
- FleetPostureSummary: active missions, degraded edge nodes, critical alerts, approval queue, failed receipts, and stale telemetry.
- MissionTable: typed columns, stable `rowKey`, `colgroup` widths, selected row, severity tags, command receipt health, filters, sorting, and bulk acknowledgement.
- NodeHealthPanel: edge node connectivity, workload, local autonomy mode, command queue depth, last sync, stale data, and disconnected offline state.
- SelectedMissionContext: selected mission summary, target preview, safety policy, agent decision run, and scoped actions.
- AlertTriage: alert timeline, critical/warning/stale/disconnected filters, AI recommendation, acknowledgement, escalation, and linked mission.
- EvidenceViewer: telemetry, logs, image snapshot, command receipt bundle, operator note, and audit trace.
- CommandApprovalDrawer: command payload, policy checks, permission-limited state, destructive confirmation, two-person approval, timeout, receipt pending, failed receipt, retry eligibility, and audit replay.
- ImplementationQuality: typed API, domain wrappers, StyleX layout tokens, Ant Design ConfigProvider theme tokens, ECharts adapter, accessibility labels, stable selectors, and Playwright screenshot hooks.

## Layout Contract

- Desktop: `CommandCenterShell` rail plus a centered page frame. The workbench grid uses primary `MissionTable` and secondary `SelectedMissionContext` columns.
- Tablet: navigation becomes a horizontal rail; workbench columns collapse into a single column without losing selected mission context.
- Mobile: rail is hidden, summary cards stack, selected mission context moves before the table, page-level overflow is hidden, and only `.table-scroll` scrolls horizontally.
- Alignment: section headers share `.section-head`; modules use the same spacing, radius, border, and shadow tokens; table columns are explicit through `colgroup`.

## Actions

- Primary action: review selected mission and request approval.
- Secondary actions: save draft, inspect evidence, acknowledge alerts, open mission, and audit receipt.
- Destructive action: block dispatch, with target, command, impact, timeout, and recovery path shown.
- Bulk action: acknowledge lower-risk queue items without changing selected mission context.

## States

- Default, selected, hover, focus, disabled, loading skeleton, empty queue, error retry, partial data, stale data, disconnected/offline node, permission-limited, command pending, receipt pending, timeout, failed receipt, success, destructive confirmation, two-person approval, and audit replay.

## Acceptance Checks

- Evaluator must include `Layout integrity and alignment`, `Module coherence and product model`, and `Responsive behavior and overflow control`.
- Keyword-only artifacts must fail marketplace grade even if they mention alignment and responsiveness.
- MAOS prototype must pass structural gates and render without page-level horizontal overflow on desktop and mobile.
- Screenshots are generated locally for desktop `1440x1000` and mobile `390x844`, then excluded from the committed marketplace package.
