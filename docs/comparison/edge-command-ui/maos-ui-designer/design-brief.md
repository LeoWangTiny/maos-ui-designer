# MAOS UI Designer Design Brief

## Audience

- Operations commander: monitors mission risk, reviews selected mission context, and approves or blocks high-risk command dispatch.
- Edge node administrator: inspects node health, stale telemetry, offline states, local autonomy, and command receipt failures.
- AI decision auditor: traces alert evidence, agent decision runs, policy checks, two-person approval, and audit replay.

## Job

Help operators review one selected high-risk mission from alert to evidence to command approval without losing alignment, context, or auditability.

## Design Context

Context: industrial IoT / command-center operational / neutral workbench palette with enterprise blue, ops amber, success green, danger red, and audit purple / responsive web app / compact daily-use density / high risk.

The first viewport is a real B2B command workbench, not a landing page. It exposes fleet posture, mission queue, selected mission context, alert triage, evidence, and command approval in one aligned review path.

## Product Model

- Primary object: selected mission `M-482`.
- Related objects: edge node `Node-A17`, alert, evidence, command payload, receipt, policy check, and agent decision run.
- Object relationship: selecting a mission drives the right context panel. Alert triage, evidence viewer, approval checks, and receipt status all share `data-context="mission:M-482"`.
- Success signal: an operator can decide whether to request approval, save a draft, or block dispatch with evidence and policy context visible.

## Layout Formation

- Layout formation: Workbench.
- Primary object: selected mission `M-482`.
- Primary region: mission queue and edge-node health.
- Secondary region: selected mission context, alert triage, evidence, command approval, receipt recovery, and audit proof.
- Actions: review selected mission in the table; request approval, save draft, and block dispatch inside the selected mission context.
- Responsive collapse: desktop two-column workbench; tablet stacked workbench; mobile context-first stack with mission table internal scroll.
- Rejected formations: dashboard + drilldown hides the selected mission; wizard / stepper is too linear for live triage; canvas + inspector is not appropriate for table-first command approval.

## Information Architecture

1. Global command shell: navigation, search, and command safety banner.
2. Fleet posture summary: active missions, degraded nodes, critical alerts, and approval queue.
3. Primary work area: mission table with explicit columns, row key, selected row, filters, sorting, and bulk action.
4. Context panel: selected mission summary, alert timeline, evidence viewer, and command approval checks.
5. Implementation guardrails: typed API, domain wrappers, stable selectors, StyleX layout tokens, Ant Design controls, ECharts adapter, and Playwright screenshot readiness.

## AI-Friendly UI Gate

- Typed API: TypeScript domain types for Mission, EdgeNode, Alert, Evidence, Command, Receipt, and AgentDecisionRun.
- UI kit: Ant Design-style B2B primitives: Table, Form, Drawer, Modal, Tabs, Tag, Badge, Timeline, Descriptions, and ConfigProvider theme tokens.
- Semantic wrappers: CommandWorkbench, FleetPostureSummary, MissionTable, NodeHealthPanel, AlertTimeline, EvidenceViewer, SelectedMissionContext, CommandApprovalDrawer, PermissionGate, and RiskStatusTag.
- Styling system: StyleX for app-owned tokenized layout, grid, spacing, radius, and responsive variants; Ant Design ConfigProvider tokens for controls.
- Stable testing: `rowKey`, `data-testid`, `data-eval-*`, `data-context`, `data-layout-role`, and deterministic desktop, tablet, and mobile viewport checks.

## Layout Quality Rules

- One selected mission context drives related modules; modules are not independent decorative cards.
- Desktop uses a two-column workbench: primary mission queue and secondary context panel.
- Table columns use `colgroup` widths so mission, node, alert, receipt, risk, and action align predictably.
- Mobile uses a task-first stack with no page-level horizontal overflow; only the mission table scrolls inside `.table-scroll`.
- Dynamic regions use stable min-height and `minmax(0, 1fr)` constraints.

## Operational States

Covered states: loading skeleton, empty queue, error retry, partial data, stale telemetry, disconnected offline node, permission-limited role gate, command pending, receipt pending, timeout, failed receipt, destructive confirmation, two-person approval, selected row, disabled action, keyboard focus, and audit replay.

## Non-Goals

- No marketing hero layout.
- No decorative dashboard made of unrelated modules.
- No color-only severity indicators.
- No page-level mobile horizontal overflow.
- No raw scattered UI kit usage without domain wrappers.
