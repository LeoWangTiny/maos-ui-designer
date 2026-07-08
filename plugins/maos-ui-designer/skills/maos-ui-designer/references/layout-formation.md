# Layout Formation

Use this reference before visual design when a screen has more than one meaningful region, action group, or responsive state. Layout formation is the page's tactical shape: what gets the field, what supports it, and how the shape changes across breakpoints.

## Formation Gate

Every non-trivial screen brief must name:

- `Primary object`: the record, task, file, mission, canvas, command, or conversation the page is organized around.
- `Primary region`: the area that owns the user's main job.
- `Secondary region`: context, detail, inspector, timeline, filters, evidence, or recovery support.
- `Actions`: where primary, secondary, bulk, and destructive actions live.
- `Responsive collapse`: desktop, tablet, and mobile behavior.
- `Rejected formations`: plausible formations that are not appropriate and why.

If the user has not chosen a formation, propose 2-3 candidates and recommend one. If speed matters, state the chosen formation as an assumption and proceed.

## Common Formations

| Formation | Use When | Avoid When |
| --- | --- | --- |
| `List + Detail` | Users choose one item from many and act on its details: tickets, tasks, approvals, assets, customers. | The primary job is broad monitoring or freeform creation. |
| `Workbench` | Users need a durable operating surface with a main work area plus context: command center, AI tool, review queue, ops console. | The page is only a metric overview with no selected object or ongoing task. |
| `Dashboard + Drilldown` | Users need posture first, then deeper investigation: analytics, health monitoring, executive or ops summaries. | Users mostly manipulate individual records repeatedly. |
| `Wizard / Stepper` | Users must complete ordered steps, high-risk confirmations, onboarding, payment, compliance, or command dispatch. | Users need fast scanning or parallel comparison. |
| `Canvas + Inspector` | Users manipulate spatial or graph objects: diagrams, flows, maps, builders, design editors. | The data is tabular and comparison-driven. |
| `Terminal/TUI Pane` | Users operate through commands, logs, keyboard focus, status bars, or pane-based terminal flows. | The surface is a visual web workflow with rich controls. |

## Output Contract

In the design brief, include this compact block:

```text
Layout formation: Workbench
Primary object: selected mission M-482
Primary region: mission queue and edge-node health
Secondary region: selected mission context, evidence, approval
Actions: review selected mission, request approval, block dispatch
Responsive collapse: desktop two-column, tablet stacked, mobile context-first with table-internal scroll
Rejected formations: dashboard + drilldown hides the selected mission; wizard / stepper is too linear for live triage
```

## Selection Rules

- Choose formation from the job, not from aesthetics.
- Put the primary object in the formation before choosing components.
- Make module relationships explicit: independent modules, selected-object modules, timeline modules, or inspector modules.
- Do not mix formations accidentally. A dashboard with a random drawer is not a workbench unless the drawer is tied to a selected object.
- Mobile behavior is part of the formation. Define what stacks, what becomes tabs, what becomes a drawer, and what may scroll internally.
- For high-risk actions, keep the action near the evidence and policy context, not isolated in a decorative toolbar.

## Common Mistakes

- Starting with cards before deciding what owns the page.
- Treating dashboards as the default for every B2B product.
- Placing every module at equal weight, causing weak hierarchy.
- Creating a rich page whose modules do not share a primary object.
- Saying "responsive" without naming the collapse order.
- Letting tables create page-level horizontal overflow on mobile instead of contained internal scroll.
