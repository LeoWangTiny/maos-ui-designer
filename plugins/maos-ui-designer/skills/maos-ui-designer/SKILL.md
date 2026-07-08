---
name: maos-ui-designer
description: End-to-end product/UI design workflow for professional frontend and interface work. Use when Codex needs to design, redesign, implement, critique, or plan app screens, SaaS dashboards, admin consoles, mobile flows, AI tools, product workflows, web UIs, CLI/TUI terminal interfaces, or frontend UI from requirements, screenshots, code, or Figma. Guides proactive clarification, industry/style/platform selection, frontend/UI framework and component-library selection under AI-friendly UI constraints, StyleX or other styling-system choices, color direction, product framing, information architecture, wireframes, visual systems, interaction states, implementation, responsive QA, and design review.
---

# MAOS UI Designer

## Purpose

Use this skill to make Codex work like a senior product designer paired with a frontend engineer. Do not jump straight to decoration. Convert the user's request into a design workflow sized to the task, then produce a product-grade interface or critique.

The goal is mature product software: clear task fit, defensible hierarchy, disciplined components, complete states, polished responsiveness, and visual choices that support real use.

## Choose The Smallest Useful Mode

- `Quick pass`: use for small UI improvements, visual polish, or a focused critique.
- `Screen workflow`: use for one page, modal, mobile screen, dashboard, form, table, editor, or settings view.
- `Product flow`: use for multi-step onboarding, checkout, AI workflow, admin process, creation flow, or approval flow.
- `Design system pass`: use when tokens, component variants, density, states, or cross-page consistency are the main issue.
- `Implementation pass`: use when the user expects code changes; design enough to make confident choices, then build and verify.

If the user asks for momentum, state assumptions and proceed. Ask at most three questions only when missing context would materially change the design.

## Clarify Before Designing

At the start of any non-trivial request, run a quick clarity scan. Actively ask concise questions when missing answers would materially change the UI, framework, or implementation path.

Ask before proceeding when:

- The target surface is unclear: web, mobile, desktop, Figma, CLI, TUI, terminal output, docs, or hybrid.
- The frontend framework or UI kit matters and cannot be inferred from the codebase.
- The user asks for AI-friendly UI, agent-editable UI, StyleX, design tokens, or a styling-system choice.
- The industry, product audience, or primary workflow is ambiguous.
- The page layout formation is ambiguous: list/detail, workbench, dashboard/drilldown, wizard, canvas/inspector, or terminal/TUI pane.
- The user asks for a style, color, or "make it professional" without enough direction.
- The request could become risky without clarification: regulated data, payments, destructive actions, permissions, operational control, or accessibility constraints.

Ask no more than three questions at once. Prefer this order:

1. `Surface and framework`: "Is this for web, mobile, CLI/TUI, or Figma, and should I use a specific UI framework?"
2. `Product context`: "What industry/user/workflow should this optimize for?"
3. `Visual direction`: "Do you want a specific style or palette, or should I choose one from the product context?"

If the codebase already answers a question, inspect it instead of asking. If the user wants speed or the missing context is low-risk, state assumptions and continue.

## Select The Design Context

Before choosing layout or visual language, identify the design axes:

- `Industry`: SaaS, finance, healthcare, developer tools, e-commerce, education, creative/media, industrial/IoT, cybersecurity, government/legal, consumer, etc.
- `Style`: operational, data-dense, editorial, brand-forward, command-center, playful, luxury/minimal, technical/developer, terminal-native, etc.
- `Palette`: neutral workbench, enterprise blue, finance green/blue, health teal, ops amber, dark technical, high-contrast terminal, brand-specific, etc.
- `Surface`: web app, responsive web, mobile app, desktop app, Figma prototype, CLI, TUI, terminal output, docs/README, or hybrid.
- `Framework`: frontend framework, UI component library, styling system, icon set, charting library, and terminal/TUI framework when relevant.
- `AI-friendly UI`: component semantics, design tokens, typed variants, testability, accessibility, and predictable styling constraints.
- `Layout formation`: list/detail, workbench, dashboard/drilldown, wizard/stepper, canvas/inspector, terminal/TUI pane, or another explicit formation.
- `Density`: compact daily-use, balanced decision surface, spacious high-stakes, presentation-grade.
- `Risk`: accessibility, regulated content, sensitive data, payment, destructive actions, operational safety.

Infer these from the product, codebase, screenshot, or user wording. If uncertain, state the chosen axes as assumptions. For detailed guidance, read `references/design-context-matrix.md` when industry, style, palette, or terminal-vs-web distinction materially affects the result.

For framework choice, prefer the existing project stack, but always place it under an AI-friendly implementation posture. If the user explicitly sets a framework, UI component library, or styling system, treat it as a hard constraint unless it conflicts with the repo or task. For greenfield work, first apply the AI-friendly gate, then choose a conservative default by surface and product type. Read `references/framework-selection.md` when the stack is unclear or the user asks to choose/set a UI framework. Read `references/ui-framework-matrix.md` when choosing a UI component library by surface or product type. Read `references/ai-friendly-ui.md` when the user asks for AI-friendly UI, agent-editable UI, StyleX, design tokens, or predictable code generation.

For non-trivial pages, read `references/layout-formation.md` before visual design. Confirm or state the layout formation before choosing detailed visual styling, cards, grids, or component composition.

## Core Workflow

### 1. Frame The Product Problem

Identify:

- Primary user, usage frequency, and usage context
- Page or flow type: dashboard, list/detail, editor, onboarding, settings, analytics, AI tool, marketplace, mobile flow, etc.
- Core job the interface must help the user complete
- Top 3 information priorities
- Primary action, secondary actions, destructive actions, and bulk actions
- Platform, responsiveness, accessibility, brand, data, and technical constraints
- Design context axes: industry, style, palette, surface, framework, AI-friendly UI posture, density, and risk
- Reference products, screenshots, Figma files, or existing code if available

### 2. Inspect The Existing Surface

When working in a codebase, inspect before designing:

- Component library, design tokens, CSS variables, theme files, spacing, typography, and icon library
- Package/dependency files that reveal the frontend framework, UI kit, styling system, StyleX/Tailwind/CSS modules setup, charting library, icons, and test tools
- Routing, layout shells, navigation, nearby pages, and established density
- Data models, permissions, empty/loading/error states, and common workflows
- Existing screenshots or browser output when visual quality matters

Prefer established local patterns. Add new primitives only when the current system cannot express the needed behavior cleanly.

### 3. Model The Product

Before layout, define the product mechanics:

- Objects: entities, records, files, users, tasks, events, commands, sessions, or results
- Relationships: hierarchy, ownership, dependencies, grouping, and lifecycle
- States: status, progress, freshness, validity, permission, risk, and failure modes
- Actions: create, edit, review, approve, retry, export, assign, compare, filter, search, undo
- Success signal: what the user can now understand or accomplish faster

For complex flows, sketch a concise flow model before the screen design. If a visual architecture or process diagram is requested, pair with a diagram/FigJam workflow instead of forcing the whole design into prose.

### 4. Confirm Layout Formation

Before visual design, choose the page formation: the tactical arrangement that decides what owns the page and what supports it.

For non-trivial screens, name:

- `Layout formation`: list/detail, workbench, dashboard/drilldown, wizard/stepper, canvas/inspector, terminal/TUI pane, or a product-specific formation.
- `Primary object`: the record, mission, task, command, canvas, conversation, or entity the page is organized around.
- `Primary region`: the area that owns the user's main job.
- `Secondary region`: context, detail, inspector, evidence, timeline, filters, or recovery support.
- `Actions`: where primary, secondary, bulk, and destructive actions live.
- `Responsive collapse`: desktop, tablet, and mobile behavior.
- `Rejected formations`: plausible formations that are not appropriate and why.

If the formation is ambiguous, propose 2-3 formations with trade-offs and recommend one. If the user wants speed, state the chosen formation as an assumption and continue. Read `references/layout-formation.md` for the formation catalog and output contract.

Do not start visual styling, decorative composition, or detailed component layout until the formation is clear.

### 5. Produce A Design Brief

For non-trivial work, write a compact brief before implementation:

- `Audience`: who uses it and how often
- `Job`: what they are trying to accomplish
- `Information hierarchy`: what must be noticed first, second, and third
- `Design context`: industry, style, palette, surface, framework, density, and risk assumptions
- `Layout formation`: chosen formation, primary object, primary region, secondary region, actions, responsive collapse, and rejected formations
- `AI-friendly UI`: component semantics, token strategy, variant API, accessibility/test hooks, and styling constraints
- `Implementation constraints`: framework, UI kit, styling system, StyleX/Tailwind/CSS modules choice, icons, charts, browser/mobile/terminal targets, and AI-friendly wrapper strategy
- `Layout`: navigation, primary region, secondary panels, toolbars, filters, tables/cards/forms, and responsive behavior
- `Actions`: primary, secondary, destructive, bulk, and contextual actions
- `States`: default, loading, empty, error, disabled, selected, hover/focus, success, partial data, permissions
- `Visual direction`: density, type scale, color roles, spacing, radius, elevation, icons, motion, imagery
- `Non-goals`: what the UI should avoid

Keep the brief short enough to guide work, not become a specification swamp.

### 6. Shape Information Architecture And Layout

Make the screen understandable before making it pretty:

- Put the real product surface in the first viewport, not a generic intro
- Make the chosen layout formation visible in the first viewport.
- Give the main work area the most space and visual clarity
- Place filters, tabs, search, sorting, object metadata, and actions where users expect them
- Separate navigation, page actions, object actions, and row/card actions
- Use tables for comparison and repeated operations; use cards for scannable objects with distinct summaries
- Define mobile behavior from the formation instead of squeezing desktop regions
- Set stable dimensions for boards, grids, toolbars, counters, tiles, and dynamic content

Do not make internal tools look like landing pages. Avoid oversized hero sections, decorative card stacks, vague marketing copy, and gradients as a substitute for structure.

### 7. Define The Visual System

Specify practical rules before decorating:

- Type hierarchy: page title, section title, body, metadata, table text, labels, buttons
- Spacing system and alignment grid
- Density: compact for repeated work, more spacious for high-stakes decisions
- Color roles: background, surface, border, text, muted text, accent, success, warning, danger
- Border radius and elevation rules
- Icon usage, tooltips for unfamiliar icon-only controls, and target sizes
- Data display: numbers, statuses, tags, timestamps, truncation, sorting, filtering, and empty values
- Accessibility: contrast, focus states, keyboard path, labels, and screen-reader names

Avoid one-note palettes, gratuitous purple/blue gradients, excessive shadows, nested cards, cramped text, and decorative elements that do not support comprehension.

### 8. Define AI-Friendly Component Architecture

Before component details, define how the interface will stay understandable to humans and AI agents:

- Use semantic component boundaries and descriptive file/component names
- Prefer typed props, explicit variants, named slots, and predictable state names
- Keep design tokens centralized and map colors to semantic roles
- Use a consistent styling system; consider StyleX when React-scale typed/static styles and tokenized variants matter
- Select UI component libraries only after checking AI-friendly maintainability: typed APIs, theme tokens, accessibility, stable composition, testability, and wrapper/adaptor strategy
- Preserve accessibility names, keyboard paths, and stable selectors for testing/automation
- Avoid ad hoc inline styles, magic numbers, and visually clever structures that obscure the product model

For deeper guidance, read `references/ai-friendly-ui.md`.

### 9. Specify Components And States

Design the behavior users will actually encounter:

- Loading, skeleton, empty, error, retry, partial data, stale data, offline, and permission-limited states
- Hover, focus, selected, disabled, success, validation, confirmation, undo, and destructive states
- Form labels, helper text, validation messages, recovery paths, and save status
- Tables/lists with sorting, filtering, selection, bulk actions, pagination/virtualization, long text, and row-level actions
- AI interfaces with input/result relationship, progress, traceability, regenerate/edit controls, history, and failure recovery

### 10. Implement Or Produce The Artifact

When implementing:

- Reuse existing components, tokens, and icon libraries first
- Follow the selected framework and UI kit idioms instead of mixing competing systems
- Wrap broad UI libraries such as Ant Design, MUI, Element Plus, or Mantine in domain components when doing so improves AI-editability and prevents scattered one-off usage
- Follow the selected styling system idioms; with StyleX, keep styles statically analyzable, token-driven, and colocated where appropriate
- Build the real first screen, not a marketing wrapper
- Include realistic content and edge-case data, not placeholder filler
- Keep copy operational and action-oriented
- Make responsive behavior explicit with stable layout constraints
- Ensure text cannot overflow or overlap controls on mobile or desktop
- Add abstractions only when they reduce real duplication or match the local design system

When producing Figma, FigJam, or design-only artifacts, keep the same product model, hierarchy, component states, and QA expectations. Use editable structure rather than flat screenshots whenever the user needs to iterate.

When designing CLI, TUI, or terminal output, optimize for command clarity, scannable text hierarchy, useful defaults, predictable flags, readable tables, non-color-dependent status, concise errors, recovery commands, and copy-pasteable examples. Choose terminal frameworks deliberately, such as Ink, Textual, Rich, Bubble Tea, or Blessed, based on the repo language and interaction model. Do not apply web-only visual assumptions to terminal interfaces.

### 11. Verify Visually

Before finalizing substantial frontend work:

- Run the app or open the artifact when possible
- Check desktop and mobile breakpoints
- Check that the chosen layout formation is visible and that modules have a clear primary/secondary relationship
- Inspect for overlap, clipping, unreadable text, unstable layout, bad focus states, and contrast issues
- Use screenshots or browser checks when practical, especially for complex or visual changes
- Fix visible issues before reporting completion

For CLI/TUI work, verify sample commands, terminal widths, wrapping, color fallbacks, help text, error output, exit codes, and copy-paste paths.

If the app needs a local dev server, start it and provide the URL after verification.

### 12. Review And Iterate

Review like a strict product designer:

- Can the target user understand where to look and what to do in five seconds?
- Is the page formation appropriate for the job, or did the page become an accidental dashboard/card pile?
- Does the screen support repeated daily use, not just presentation?
- Are real states, errors, edge cases, permissions, and responsive layouts handled?
- Does anything look generic, decorative, unaligned, low-contrast, cramped, or template-like?
- Would the UI still work with long names, empty data, missing permissions, or slow networks?

For layout formation, read `references/layout-formation.md`. For design context selection, read `references/design-context-matrix.md`. For framework selection, read `references/framework-selection.md`. For UI component-library selection by endpoint/product type, read `references/ui-framework-matrix.md`. For AI-friendly UI and StyleX guidance, read `references/ai-friendly-ui.md`. For a full workflow checklist, read `references/design-workflow-checklist.md`. For deeper critique, read `references/ui-quality-rubric.md`.

## Tool Pairing

- Use Figma design skills when the user wants editable design files, design systems, or Figma-to-code work.
- Use diagram/FigJam skills when the user asks for architecture diagrams, process maps, system flows, or complex visual explanations.
- Use Playwright or screenshot skills when verifying implemented frontend changes.
- Use accessibility or security skills when the surface includes auth, permissions, sensitive data, payments, or high-risk workflows.

## Response Patterns

For planning-only requests, return the design brief, key assumptions, and the smallest next design step.

For implementation requests, briefly present the design direction, implement the page, verify visually when practical, then summarize what changed and what was checked.

For critique requests, lead with findings ordered by severity, include concrete fixes, and apply the fixes if the user asked for changes.

For full workflow requests, move through: select context, frame, inspect, model, confirm layout formation, brief, layout, visual system, states, implementation or artifact, visual QA, review.
