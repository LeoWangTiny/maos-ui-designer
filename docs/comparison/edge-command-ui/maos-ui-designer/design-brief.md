# MAOS UI Designer Design Brief

## Audience

- Operations commander: monitors fleet posture, triages critical alerts, drafts and dispatches approved commands.
- Edge node administrator: inspects node health, local autonomy mode, disconnected states, and command relay issues.
- Device maintenance operator: reviews device evidence, acknowledges maintenance tasks, and follows recovery paths.
- AI decision auditor: reviews agent decision runs, evidence, policy checks, overrides, receipts, and audit replay.

## Job

Help operators understand operational risk, triage alert evidence, and approve or block high-risk command dispatch without losing auditability.

## Design Context

Context: industrial IoT / command-center operational / neutral workbench palette with enterprise blue, ops amber, success green, danger red, and semantic status colors / responsive web app / compact daily-use density / high risk.

The page is not a landing page. The first viewport must show the real product surface: fleet posture, active missions, degraded edge nodes, critical alerts, pending approvals, failed command receipts, and the current command safety state.

## AI-Friendly UI Gate

- Typed API: TypeScript domain types for Mission, EdgeNode, Device, Alert, Command, Receipt, Evidence, and AgentDecisionRun.
- UI kit: Ant Design-style B2B primitives: Table, Form, Drawer, Modal, Tabs, Tag, Badge, Timeline, Descriptions, and ConfigProvider theme tokens.
- Semantic wrappers: CommandCenterShell, FleetPostureSummary, MissionTable, NodeHealthPanel, AlertTimeline, EvidenceViewer, CommandApprovalDrawer, PermissionGate, RiskStatusTag.
- Styling system: StyleX for app-owned tokenized layout and typed variants; Ant Design ConfigProvider theme tokens for controls.
- Charts: ECharts or AntV through typed chart adapters for node health, alert trend, topology, and command receipt timeline.
- Accessibility: keyboard focus, visible labels, non-color-only states, clear destructive confirmation, and screen-reader friendly status names.
- Stable testing: `data-testid`, `data-eval-*`, stable `rowKey`, deterministic fixtures, desktop and mobile screenshots.

## Product Priorities

1. Operational posture: degraded nodes, disconnected devices, critical alerts, active missions, and failed command receipts.
2. Safe action: permission-limited actions, policy checks, destructive confirmation, two-person approval, timeout, receipt pending, failed recovery.
3. Audit confidence: evidence, AI recommendation, receipt trail, policy checks, human override, and replay export.

## Non-Goals

- No marketing hero layout.
- No decorative gradient dashboard as the main concept.
- No raw scattered UI kit usage without domain wrappers.
- No color-only severity indicators.
