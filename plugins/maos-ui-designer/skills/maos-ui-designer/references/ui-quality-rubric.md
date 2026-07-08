# UI Quality Rubric

Use this reference when reviewing a generated or implemented app screen for maturity.

## Product Fit

- The screen has a clear primary user, job, and frequency of use.
- The first viewport reveals the actual product surface, not a generic hero or decorative intro.
- Primary and secondary actions match the user's real workflow.
- The design distinguishes daily-use productivity from marketing presentation.

## Information Architecture

- The most important information is visually dominant for a defensible reason.
- Related controls and data are grouped together.
- Filters, search, tabs, actions, and object metadata sit where users expect them.
- Labels are specific and operational, not vague or decorative.

## Layout Formation

- The page has a named formation: list/detail, workbench, dashboard/drilldown, wizard/stepper, canvas/inspector, terminal/TUI pane, or a clear product-specific formation.
- The primary object, primary region, secondary region, action placement, and responsive collapse are explicit.
- Plausible but wrong formations are rejected with a reason.
- Modules share the formation instead of forming an accidental dashboard or card pile.

## Layout and Density

- Alignment is crisp across headings, controls, tables, cards, and panels.
- Density matches task frequency: repeated work is compact; high-stakes decisions get more breathing room.
- No cards inside cards unless there is a strong product reason.
- Responsive layouts define stable dimensions and do not allow text or controls to collide.

## Component Craft

- Buttons use clear hierarchy: primary, secondary, tertiary, destructive.
- Icon-only controls have familiar icons and tooltips.
- Forms include labels, validation, disabled states, helper text where useful, and recovery paths.
- Tables/lists handle sorting, filtering, selection, bulk actions, long text, empty data, and partial loading.

## Visual System

- Typography has a restrained scale and fits the density of the surface.
- Color roles are consistent and semantic.
- Borders, shadows, and radius are subtle and system-like.
- The palette is not dominated by a single hue family unless brand constraints require it.
- Imagery, if used, helps inspect the product, object, user, place, or state.

## Interaction States

- Loading, empty, error, success, disabled, hover, focus, selected, and permission-limited states are represented.
- Destructive actions include clear confirmation or undo when appropriate.
- Long-running actions expose progress or status.
- Keyboard and screen-reader paths are considered for core workflows.

## Common Maturity Problems

- Looks like a landing page instead of an app.
- Too many decorative cards, gradients, oversized headings, or vague badges.
- Weak data hierarchy: everything has the same visual weight.
- Missing page formation: modules are rich but do not know their positions or relationships.
- Real workflow states are missing.
- Copy explains the UI instead of helping the user act.
- Mobile layout is just a squeezed desktop layout.
- Components feel invented one-off instead of part of a system.

## Review Output Format

When reviewing, use:

1. `Critical fixes`: issues that block comprehension, task completion, accessibility, or responsiveness.
2. `Maturity improvements`: changes that make the UI feel more product-grade.
3. `Polish`: small alignment, copy, density, icon, and visual refinements.
4. `Recommended next pass`: the smallest set of edits that would most improve the page.
