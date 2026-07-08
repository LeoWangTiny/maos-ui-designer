# AI-Friendly UI

Use this reference when the user asks for AI-friendly UI, agent-editable frontend architecture, design-token discipline, StyleX, or UI that future agents can safely inspect, modify, and test.

## Goal

Design UI so both humans and AI agents can understand the product model, find the right component, change the right style, and verify behavior without guessing.

## Principles

- Use semantic component names that match product objects and actions.
- Keep components small enough to understand but not fragmented into decorative pieces.
- Prefer explicit props, typed variants, named slots, and predictable state names.
- Centralize design tokens for color, spacing, radius, typography, elevation, and motion.
- Map colors to roles such as `surface`, `text`, `muted`, `accent`, `success`, `warning`, and `danger`.
- Keep accessibility names, labels, roles, focus states, and keyboard paths clear.
- Provide stable selectors or test hooks according to project convention.
- Avoid arbitrary magic numbers, scattered inline styles, and one-off visual exceptions.

## Framework Selection Gate

Choose UI frameworks and component libraries through this gate before applying industry defaults:

- `Typed API`: TypeScript or equivalent type contracts for props, events, forms, tables, and variants.
- `Token/theming`: centralized color, spacing, typography, radius, elevation, and motion tokens.
- `Semantic wrappers`: ability to wrap generic components in product/domain components.
- `Accessibility`: keyboard paths, labels, roles, focus states, and documented a11y behavior.
- `Predictable styling`: one styling system, limited overrides, no scattered magic numbers.
- `Stable testing`: stable selectors, row keys, form names, and screenshot-friendly states.
- `Documentation gravity`: enough examples and conventions for agents to infer correct usage.

If a product-type default such as Ant Design is selected, still use it through this gate. For example, prefer `UserTable`, `OrderApprovalForm`, or `RiskStatusTag` wrappers over scattering raw `Table`, `Form`, and `Tag` usage across the app.

## StyleX Guidance

StyleX is a styling system, not a full UI component library. Use it with React/Next.js and headless or local components when the project benefits from typed, tokenized, statically analyzable styles.

Prefer StyleX when:

- The UI will be frequently edited by agents or multiple developers.
- The project needs strong design-token discipline and predictable style composition.
- The app is React-based and can support StyleX build tooling.
- The design system should colocate component styles while keeping constraints explicit.

Use StyleX carefully:

- Define shared tokens and themes before scattering component styles.
- Keep `stylex.create` objects named by intent, not by visual accident.
- Use variants through typed props and small style arrays.
- Keep dynamic styling limited to explicit states and token choices.
- Do not use StyleX as a substitute for product hierarchy, accessibility, or component design.

## Good AI-Editable Component Shape

Use patterns like:

```tsx
type StatusTone = "neutral" | "success" | "warning" | "danger";

type StatusBadgeProps = {
  label: string;
  tone?: StatusTone;
};
```

Then map `tone` to semantic styles, not raw colors. This gives future agents a small, safe edit surface.

## AI-Friendly Brief Additions

Add these lines to the design brief when relevant:

- `AI-editability`: what future agents should be able to change safely.
- `Token strategy`: where colors, spacing, typography, and themes live.
- `Variant model`: which visual states are encoded as typed variants.
- `Testing hooks`: how screenshots, accessibility checks, and selectors verify the UI.
- `Style system`: StyleX, Tailwind, CSS modules, CSS variables, or existing system.

## Review Checklist

- Can an agent identify the main product objects from component and file names?
- Can it change a visual role without hunting through unrelated CSS?
- Are design tokens named semantically rather than by raw color?
- Are variants explicit rather than encoded in duplicated markup?
- Does the UI remain accessible and testable after style changes?
- Are framework and styling-system idioms used consistently?
