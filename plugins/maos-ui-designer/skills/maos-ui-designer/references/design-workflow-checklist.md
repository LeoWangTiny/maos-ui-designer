# Design Workflow Checklist

Use this reference when the user asks for a complete design workflow, a major redesign, or a professional frontend design pass that should go beyond a single critique.

## Intake

- Define the target user, task frequency, and usage context.
- Name the product object being manipulated or inspected.
- Identify the top 3 decisions or actions the interface must support.
- Note hard constraints: platform, brand, existing components, accessibility, data availability, and deadlines.

## Design Context

- Select industry: SaaS, finance, healthcare, developer tools, e-commerce, education, creative/media, industrial/IoT, cybersecurity, government/legal, consumer, or other.
- Select style: operational, data-dense, editorial, brand-forward, command-center, playful, luxury/minimal, technical/developer, terminal-native, or other.
- Select palette direction: neutral workbench, enterprise blue, finance green/blue, health teal, ops amber, dark technical, high-contrast terminal, brand-specific, or other.
- Select surface: web app, responsive web, mobile app, desktop app, Figma prototype, CLI, TUI, terminal output, docs/README, or hybrid.
- Select framework constraints: frontend framework, UI kit, styling system, icons, charts, and terminal/TUI library when relevant.
- Select AI-friendly UI constraints: semantic component boundaries, token strategy, typed variants, stable selectors, accessibility, and predictable styling.
- State assumptions when the user does not specify these axes.

## Clarifying Questions

- Ask up to three concise questions when surface, framework, styling system, AI-friendly UI requirements, user/workflow, style, palette, or risk is ambiguous.
- Inspect the codebase before asking about framework if files such as `package.json`, lockfiles, app config, or component directories are available.
- Prefer assumptions over questions for low-risk polish tasks.
- Treat user-specified framework, UI kit, style, or palette as constraints unless they conflict with the existing project.

## Product Model

- List core objects and their relationships.
- List object states and lifecycle stages.
- List primary, secondary, bulk, destructive, and recovery actions.
- Identify permission levels and collaboration touchpoints.
- Clarify what success looks like after the user completes the workflow.

## Research And References

- Inspect existing app screens and local design tokens.
- Use supplied screenshots, Figma files, specs, or competitor references when available.
- Extract patterns, not decoration: navigation, density, data hierarchy, action placement, state handling, and copy tone.
- State assumptions when references are unavailable.

## Information Architecture

- Decide the navigation level: app shell, section, page, panel, modal, drawer, or stepper.
- Group information by task, object, status, ownership, or time.
- Place search, filters, sort, tabs, and actions in predictable locations.
- Separate global actions from object-level and row-level actions.
- Define how users move forward, back, cancel, retry, and recover.

## Layout

- Establish the primary work area and secondary support areas.
- Choose table, list, card, timeline, board, canvas, or form layouts based on the job.
- Define responsive behavior for mobile, tablet, and desktop.
- Reserve stable dimensions for dynamic regions.
- Avoid nested cards, oversized headings in compact surfaces, and decorative containers.

## Visual System

- Define typography roles and scale.
- Define spacing, radius, border, and elevation rules.
- Define semantic color roles and keep accent colors purposeful.
- Choose icons for recognition, not decoration.
- Ensure contrast, focus states, target sizes, and keyboard paths are acceptable.

## Components And States

- Include default, loading, empty, error, disabled, selected, hover, focus, success, and permission-limited states.
- Include validation, helper text, destructive confirmation, undo, retry, and partial data where relevant.
- For tables and lists, handle sorting, filtering, pagination, selection, bulk actions, truncation, and long labels.
- For AI workflows, include processing, provenance, regeneration, editing, history, and failure recovery.

## Implementation

- Reuse the local component library, tokens, icons, and layout conventions.
- Follow the selected framework and UI kit idioms; do not mix incompatible component systems without a reason.
- Follow the selected styling system. For StyleX, keep styles tokenized, statically analyzable, and composed through explicit style objects.
- Implement realistic data, including edge cases.
- Keep text concise and operational.
- Use stable responsive constraints so content does not shift or collide.
- Avoid broad refactors unless the design cannot be implemented safely without them.
- For CLI/TUI, verify commands, flags, help, output hierarchy, wrapping, color fallbacks, errors, and exit codes.

## Verification

- Check desktop and mobile screenshots when practical.
- Inspect alignment, overflow, clipping, contrast, focus, loading states, and empty/error states.
- Verify that the first viewport exposes the real workflow.
- Confirm that the primary action is obvious and secondary actions are not competing.
- Iterate before final response when visible defects are found.

## Handoff

- Summarize the design direction.
- Mention implementation files or artifacts changed.
- State what was visually verified and what was not.
- List only the highest-value next pass, if one remains.
