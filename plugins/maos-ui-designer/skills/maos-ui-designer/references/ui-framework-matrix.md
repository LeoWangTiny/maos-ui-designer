# UI Framework Matrix

Use this reference when selecting a UI framework or component library. The rule is strict: choose frameworks inside an AI-friendly UI posture. Product-type defaults are recommendations, not permission to create hard-to-maintain UI.

## AI-Friendly Gate

Before selecting a library, check:

- Type-safe APIs or clear contracts
- Theme tokens or design-token integration
- Semantic wrapper/adaptor strategy
- Accessibility and keyboard behavior
- Stable selectors and predictable DOM for tests
- Consistent styling system with limited overrides
- Good examples and conventions for future agents

If the existing project already uses a weaker library, keep it unless the user asks for migration, but add a domain wrapper layer and token conventions.

## Web B2B / Admin / Management

Default choices:

- `React`: Ant Design, Arco Design, Semi Design, MUI/MUI X, Mantine
- `Vue`: Element Plus, Naive UI, Ant Design Vue, Vuetify
- `Angular`: NG-ZORRO, Angular Material

Recommended defaults:

- For React B2B/admin in Chinese or enterprise-heavy contexts: `Ant Design + TypeScript + ConfigProvider/theme tokens + typed domain wrappers`.
- For CRUD-heavy React admin: add `ProComponents` or a local table/form schema layer only when it reduces duplication.
- For Vue admin: `Element Plus + TypeScript + tokenized theme + typed domain wrappers`.

AI-friendly constraints:

- Wrap generic primitives as product components: `AssetTable`, `UserPermissionForm`, `ApprovalTimeline`, `RiskStatusTag`.
- Use typed table columns, typed form schemas, stable `rowKey`, explicit empty/loading/error states, and clear permission states.
- Put theme overrides in one place. Avoid scattered CSS overrides against library internals.
- Use chart adapters for ECharts/AntV/Recharts instead of inline chart config in pages.

## Web SaaS / Product Tools / AI Apps

Default choices:

- `Next.js + TypeScript + Tailwind + shadcn/ui`
- `React/Next.js + TypeScript + StyleX + Radix/headless primitives`
- `React + Mantine`
- `React + Chakra UI`
- `React + MUI`

Recommended defaults:

- For AI/SaaS products where examples and speed matter: `Next.js + shadcn/ui + Tailwind`.
- For AI-editable React design systems where tokenized static styles matter: `React/Next.js + StyleX + Radix/headless components`.
- For broad component coverage with less custom composition: `Mantine`, `Chakra`, or `MUI`.

AI-friendly constraints:

- Define typed variants for cards, badges, empty states, AI message panels, result cards, and toolbars.
- Keep prompts, runs, traces, histories, and generated outputs as named product components.
- Expose loading, streaming, retry, regenerate, edit, failure, and provenance states.

## Web Consumer / Landing / Brand

Default choices:

- Tailwind CSS
- shadcn/ui
- HeroUI/NextUI
- Framer Motion
- Carefully selected local components

AI-friendly constraints:

- Even expressive pages need semantic sections: `Hero`, `FeatureGrid`, `PricingPlans`, `ProofStrip`, `FAQ`.
- Keep brand tokens centralized. Avoid one-off animation or gradient snippets scattered through pages.
- Use generated or real assets deliberately; keep layout editable and testable.

## Data Visualization / Command Center / Monitoring

Default choices:

- UI shell: Ant Design, Arco Design, MUI, Mantine, or local system
- Charts: ECharts, AntV, Recharts, D3 when custom visualization is central
- Maps/canvas: Mapbox, Deck.gl, custom canvas/WebGL when needed

Recommended defaults:

- Dense ops dashboards: `Ant Design or Arco + ECharts/AntV + typed chart adapters`.
- Product dashboards: `shadcn/ui or Mantine + Recharts` when charts are straightforward.

AI-friendly constraints:

- Use typed chart data adapters and named chart components.
- Keep severity, freshness, status, and alert colors semantic.
- Provide empty, partial, stale, loading, and disconnected states.

## Mobile H5 / Responsive Web

Default choices:

- `Vue`: Vant, Varlet
- `React`: Ionic React, Tailwind/shadcn adapted carefully
- `Cross-framework`: Ionic

AI-friendly constraints:

- Prioritize touch targets, step clarity, validation, offline/loading states, and bottom action placement.
- Keep mobile-specific components separate from squeezed desktop components.

## Native Mobile

Default choices:

- `React Native`: React Native Paper, Tamagui, NativeWind, React Native Elements
- `Flutter`: Material 3, Cupertino, Fluent UI for Flutter

AI-friendly constraints:

- Keep tokens shared or mapped from the design system.
- Use typed navigation routes, typed screen props, stable test IDs, and explicit loading/error/offline states.

## Desktop

Default choices:

- `Electron/Tauri + React`: Ant Design, MUI, shadcn/ui, Mantine
- `Flutter Desktop`: Material 3, Fluent UI
- `.NET/Windows`: WinUI, Fluent UI

AI-friendly constraints:

- Account for resizable panels, local file states, menu/toolbars, keyboard shortcuts, and long-running actions.
- Keep platform affordances explicit instead of copying web layout blindly.

## CLI / TUI / Terminal

Default choices:

- `Node.js`: Ink, Blessed
- `Python`: Textual, Rich
- `Go`: Bubble Tea
- `Rust`: Ratatui

AI-friendly constraints:

- Design command names, flags, help text, output hierarchy, wrapping, color fallback, exit codes, and recovery commands.
- Use structured output modes such as JSON when automation matters.
- Keep terminal UI readable without color.

## Styling Pairings

- `Ant Design`: ConfigProvider/theme tokens + domain wrappers + CSS modules or project styling for app-owned layout.
- `MUI`: theme tokens + typed wrappers + MUI X only when data-grid complexity justifies it.
- `shadcn/ui`: Tailwind tokens + typed variants + local component ownership.
- `StyleX + Radix`: tokenized static styles + headless accessible primitives + typed variants.
- `Element Plus`: theme variables + typed wrappers + schema-driven forms/tables.

## Default Decision Examples

- `Web / B2B admin / React`: Ant Design + TypeScript + theme tokens + domain wrappers + ECharts/AntV if needed.
- `Web / AI SaaS / Next.js`: shadcn/ui + Tailwind, or StyleX + Radix when AI-editability and static style discipline are more important than ready-made components.
- `Web / monitoring command center`: Ant Design or Arco + ECharts/AntV + typed severity/status components.
- `CLI / Python`: Textual for interactive TUI, Rich for command output.
- `Mobile H5 / Vue`: Vant or Varlet with explicit mobile workflow components.
