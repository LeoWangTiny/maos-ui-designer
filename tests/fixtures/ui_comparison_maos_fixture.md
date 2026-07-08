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
<style>
  :root { --space-3: 12px; --space-4: 16px; --radius-panel: 8px; --border: #d8e0eb; }
  body { width: 100%; max-width: 100%; overflow-x: hidden; }
  .workbench-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(340px, 380px); gap: var(--space-4); }
  .section-head { min-height: 44px; display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; }
  .table-scroll { overflow-x: auto; }
  @media (max-width: 1100px) { .workbench-grid { grid-template-columns: 1fr; } }
  @media (max-width: 720px) { .summary-grid { grid-template-columns: 1fr; } }
</style>
<main data-eval-artifact="maos-ui-designer" data-layout="command-workbench" data-responsive-strategy="desktop-rail tablet-stack mobile-task-first" data-selected-mission="M-482" data-design-context="industrial-iot command-center responsive-web high-risk" data-ai-friendly="tokens wrappers rowKey data-testid accessibility">
  <section data-testid="command-center-overview" data-component="CommandCenterOverview" data-layout-role="primary" data-context="mission:M-482" data-module-purpose="mission queue and posture">
    <div class="section-head"><h2>Selected mission queue</h2><button data-primary-action="review-selected-mission">Review selected mission</button></div>
    <div data-component="FleetPostureSummary">Degraded nodes, critical alerts, pending approvals, failed receipts</div>
    <div class="table-scroll">
      <table data-component="MissionTable" data-row-key="missionId">
        <colgroup>
          <col data-column="mission" style="width: 28%">
          <col data-column="edge-node" style="width: 18%">
          <col data-column="alert" style="width: 22%">
          <col data-column="receipt" style="width: 18%">
          <col data-column="risk" style="width: 14%">
        </colgroup>
        <tr><th>Mission</th><th>Edge Node</th><th>Alert</th><th>Command Receipt</th><th>Risk</th></tr>
      </table>
    </div>
  </section>
  <aside data-testid="selected-mission-context" data-component="SelectedMissionContext" data-layout-role="context" data-context="mission:M-482" data-mobile-order="mobile-context-first" data-module-purpose="selected mission evidence and approval">
    <div class="section-head"><h2>Selected mission M-482</h2><span>high risk</span></div>
    <section data-testid="alert-triage" data-component="AlertTriage" data-context="mission:M-482" data-module-purpose="alert evidence">
      <div data-component="AlertTimeline">critical warning stale disconnected evidence AI recommendation escalation</div>
      <div data-component="EvidenceViewer">telemetry logs image snapshot audit trace</div>
    </section>
    <section data-testid="command-approval-drawer" data-component="CommandApprovalDrawer" data-context="mission:M-482" data-action-scope="selected mission" data-module-purpose="command approval">
      <button>Request approval</button>
      <button>Block dispatch</button>
      <div data-state="permission-limited">Role gate requires commander approval</div>
      <div data-state="destructive-confirmation">Confirm target and command impact</div>
      <div data-state="two-person-approval">Requester and approver required</div>
      <div data-state="receipt-pending">Command pending, timeout countdown active</div>
      <div data-state="failed">Failed receipt recovery path</div>
    </section>
  </aside>
</main>
```
