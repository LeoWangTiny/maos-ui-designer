# Framework Selection

Use this reference when the user asks to set a frontend UI framework, when a greenfield implementation needs a stack, or when the existing codebase does not make the UI framework obvious.

## Selection Order

1. Apply the AI-friendly gate: type safety, semantic components, token/theming support, accessibility, predictable styling, stable selectors, and testability.
2. Use the framework already present in the repo, adding wrappers/adapters if needed to make it agent-maintainable.
3. Use the framework explicitly requested by the user.
4. Choose the most conservative framework for the product, team, and surface.
5. Avoid migrations or adding a second UI system unless the user asked for it or the existing system cannot support the design.

## Inspect Before Asking

Check for:

- `package.json`, lockfiles, `vite.config.*`, `next.config.*`, `nuxt.config.*`, `svelte.config.*`, `angular.json`, `astro.config.*`
- `src/components`, `app/`, `pages/`, `components/ui`, `styles`, `tailwind.config.*`, `postcss.config.*`
- Dependencies such as React, Next.js, Vue, Nuxt, Svelte, Angular, Tailwind, StyleX, shadcn/ui, Radix, MUI, Ant Design, Chakra, Mantine, Bootstrap, DaisyUI, Headless UI, Lucide, Recharts, ECharts, D3

If inspection answers the framework question, state the detected stack and proceed.

## Web Defaults

- `Next.js + TypeScript + Tailwind + shadcn/ui`: good default for polished SaaS, dashboards, AI tools, admin apps, and product surfaces.
- `React + Vite + TypeScript + Tailwind`: good for lightweight apps, prototypes, static tools, and custom UI.
- `React + MUI`: good for enterprise apps that need mature components, data grids, theming, and accessibility.
- `React + Ant Design`: good for dense admin systems, CRUD-heavy dashboards, and enterprise workflows.
- `React + Mantine`: good for fast product UI with many polished components and hooks.
- `React + Chakra`: good for accessible component composition and design-system-friendly apps.
- `Vue + Nuxt`: good for content-heavy apps, dashboards, and teams already using Vue.
- `Vue + Element Plus` or `Naive UI`: good for admin dashboards and enterprise Vue apps.
- `SvelteKit`: good for lightweight, expressive apps where simple interactivity and performance matter.
- `Angular + Material`: good for large enterprise teams, strict structure, and long-lived applications.

For endpoint/product-type defaults, read `ui-framework-matrix.md`.

## Styling And Components

- Use `Tailwind` when custom composition, utility workflow, and responsive tuning matter.
- Use `StyleX` when React-scale typed/static styling, design-token discipline, deterministic composition, and AI-editable style objects matter. Treat it as a styling system, not a component library.
- Use `shadcn/ui` when the app needs editable, product-grade React components with Tailwind.
- Use `Radix` or `Headless UI` when accessibility and custom styling matter more than prebuilt visuals.
- Use `MUI`, `Ant Design`, `Mantine`, or `Chakra` when delivery speed and complete component coverage matter.
- Use one primary component system. Mixing multiple UI kits usually creates inconsistent spacing, states, and theming.

## AI-Friendly UI Defaults

- Prefer explicit component APIs, typed variants, named tokens, and semantic DOM.
- Prefer styling systems that keep intent readable and constrain arbitrary visual drift.
- For React greenfield projects where AI will frequently modify UI, consider `React/Next.js + TypeScript + StyleX + Radix/headless primitives` or `Next.js + TypeScript + Tailwind + shadcn/ui`.
- Choose StyleX for tokenized static style objects; choose Tailwind/shadcn when component availability and common examples matter more.

## Charts, Icons, Tables

- Use `lucide-react` or the repo's existing icon set for app UI.
- Use `Recharts` for straightforward dashboard charts.
- Use `ECharts` for dense analytics, monitoring, finance, and complex interactions.
- Use `D3` only when custom visualization is central to the product.
- Use the existing table/grid system first; otherwise choose based on scale and complexity.

## Mobile And Desktop

- `React Native` or `Expo`: mobile apps with React teams and rapid iteration.
- `Flutter`: highly custom cross-platform mobile or desktop surfaces.
- `Electron` or `Tauri`: desktop apps that need local system integration.
- For mobile web, prefer responsive web patterns before introducing a native stack.

## CLI, TUI, And Terminal

- `Ink`: React-style CLI/TUI for Node.js projects.
- `Textual`: rich Python TUI apps with panels, keyboard navigation, and async workflows.
- `Rich`: Python terminal output, tables, progress bars, logs, and readable CLI feedback.
- `Bubble Tea`: Go TUI apps with strong keyboard-driven interaction.
- `Blessed`/`blessed-contrib`: Node terminal dashboards and legacy terminal UIs.

For terminal surfaces, design command structure, help text, output hierarchy, wrapping, color fallback, exit codes, and recovery messages before thinking about visual flourish.

## Clarifying Question

When framework is unknown and matters, ask:

`Should I use the existing stack, or do you want a specific UI framework/styling system such as Next.js + shadcn/ui, React + StyleX, React + MUI, React + Ant Design, Vue + Element Plus, or a CLI/TUI framework?`
