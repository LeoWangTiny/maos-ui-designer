# MAOS UI Designer Artifact

## Brief

Context: industrial IoT / command-center operational / neutral workbench palette with enterprise blue, ops amber, success green, and danger red / responsive web app / compact daily-use density / high risk.

AI-friendly UI gate: typed API, TypeScript table columns, semantic tokens, domain wrappers, accessibility labels, keyboard focus, stable selectors, `rowKey`, and `data-testid` hooks.

Framework choice: React + TypeScript with Ant Design-style Table, Form, Drawer, Modal, Tabs, Tags, Timeline, and ConfigProvider theme tokens. Use StyleX for app-owned tokenized layout and ECharts chart adapters for dense operational charts.

## Screen Spec

- Command Center Overview: fleet health, active missions, degraded edge nodes, critical alerts, pending approvals, failed command receipts, topology map, mission queue, and AI decision summary.
- Alert Triage: severity filters, alert timeline, evidence viewer, associated mission/device, AI recommendation, acknowledgement, escalation, and command draft.
- Command Approval Drawer: target preview, command payload, policy checks, permission-limited states, destructive confirmation, two-person approval, timeout, receipt pending, failed receipt, and audit replay.
- Required operational states: loading skeleton, empty queue, error retry, partial data, stale telemetry, disconnected offline node, permission-limited role gate, command pending, receipt pending, timeout, failed receipt, destructive confirmation, and two-person approval.
- Screenshot readiness: Playwright captures desktop, tablet, and mobile viewport screenshots; the prototype includes stable `data-eval-*` and `data-testid` attributes for comparison.

## HTML Markers

```html
<main data-eval-artifact="maos-ui-designer" data-design-context="industrial-iot command-center responsive-web high-risk" data-ai-friendly="tokens wrappers rowKey data-testid accessibility">
  <section data-testid="command-center-overview" data-component="CommandCenterOverview">
    <div data-component="FleetPostureSummary">Degraded nodes, critical alerts, pending approvals, failed receipts</div>
    <table data-component="MissionTable" data-row-key="missionId">
      <tr><th>Mission</th><th>Edge Node</th><th>Alert</th><th>Command Receipt</th><th>Risk</th></tr>
    </table>
  </section>
  <section data-testid="alert-triage" data-component="AlertTriage">
    <div data-component="AlertTimeline">critical warning stale disconnected evidence AI recommendation escalation</div>
    <div data-component="EvidenceViewer">telemetry logs image snapshot audit trace</div>
  </section>
  <aside data-testid="command-approval-drawer" data-component="CommandApprovalDrawer">
    <div data-state="permission-limited">Role gate requires commander approval</div>
    <div data-state="destructive-confirmation">Confirm target and command impact</div>
    <div data-state="two-person-approval">Requester and approver required</div>
    <div data-state="receipt-pending">Command pending, timeout countdown active</div>
    <div data-state="failed">Failed receipt recovery path</div>
  </aside>
</main>
```
