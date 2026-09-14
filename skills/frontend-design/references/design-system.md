# Visual system

## Palette and roles

Muted and semantic colors are tuned for readability.

| Role | Value | Use |
| --- | --- | --- |
| Site background | `#fcfafb` | Large open areas |
| App background | `#faf8f9` | Workspace |
| Surface | `#ffffff` | Panels, lists, dialogs |
| Main text | `#29242a` | Headings and content |
| Secondary text | `#74616c` | Captions, hints |
| Main accent | `#e47f93` | Primary button, a single visual accent |
| Text on accent | `#392029` | Label of the pink button |
| Deep rose | `#a94460` | Links, focus, active text |
| Dark rose | `#9a3f55` | Selected navigation, outlined buttons |
| Soft rose | `#fcecf0` | Background of a selection or an icon |
| Plum | `#9272a8` | Secondary branch of a diagram, illustration |
| Soft plum | `#f2edf8` | Additional surface |
| Site border | `#eee4e9` | Decorative separation of surfaces |
| Row border | `#e9edf2` | Row dividers |

A light border separates areas, but on its own it does not make a control recognizable. Give controls a shape, a label, a visible marker and a darker border. The plum and pink accents are not meant for small text on white; the CSS has separate dark tokens for that.

## Scale

- Spacing grid: 4, 8, 12, 16, 24, 32, 48, 64, 96 px.
- Landing content up to 1200-1280 px, side margins 24-48 px; mobile margins 16-24 px.
- Landing page: heading `clamp(2.75rem, 7vw, 7rem)`, line-height 1.04-1.1, tracking about `-.045em`.
- App: heading 28-32 px, content 14-16 px, captions 12-14 px, line-height 1.45-1.65.
- Font: system UI, Segoe UI, Arial; Inter when the project already has it. Check that the font covers the interface language. A well-tuned ordinary sans-serif fits this look, an unusual font is not required.
- Radii: 10-12 px for icon tiles and small fields, 14-18 for buttons and lists, 20-24 for large panels. Keep pills for short segments and statuses.
- Icons: 20-24 px, stroke 1.6-1.8, rounded caps, currentColor. Use the project's existing icon library; do not mix emoji with several incompatible sets.
- Motion: 140-220 ms in response to an action. A small shift is fine on a button, but not every block should bounce. A faint local glow around a demo is fine, a site-wide gradient is not needed.

## Two layouts from one family

### Landing page

Short navigation, a concise heading with the main action, visual proof or an interactive example, only the necessary explanations, a simple footer. These are roles, not one required section each. The demo can sit to the right of the text, or the image can lead.

The starter `${CLAUDE_SKILL_DIR}/assets/interactive-starter.html` shows day planning, where choosing a rhythm changes the preview. It shows how the style fits a specific subject area. The starter opens directly in a browser next to `tokens.css` and needs no external libraries, fonts or network.

### Working interface

A moderately narrow white navigation, a light canvas, a heading and one main action, then useful content. A list can be one panel with dividers. The active section gets a soft rose background and a dark rose label. On mobile the navigation becomes a short row or a collapsible menu, depending on how complex the product is.

Layout example (fill in real URLs and content):

```html
<div class="fd-app">
  <nav class="fd-nav" aria-label="Sections">
    <a href="/today" aria-current="page">Today</a>
    <a href="/library">Library</a>
  </nav>
  <main class="fd-main">
    <h1>Today</h1>
    <!-- The product's main scenario and an action with a real handler go here. -->
  </main>
</div>
```

```css
.fd-app { min-height: 100svh; display: grid; grid-template-columns: 226px minmax(0, 1fr); background: var(--fd-bg-app); }
.fd-nav { padding: 32px 16px; background: var(--fd-surface); border-right: 1px solid var(--fd-line-app); }
.fd-nav a { display: block; padding: 14px 16px; border-radius: var(--fd-radius-sm); color: var(--fd-muted); text-decoration: none; }
.fd-nav a[aria-current="page"] { color: var(--fd-rose-strong); background: var(--fd-rose-soft); font-weight: 600; }
.fd-main { min-width: 0; padding: clamp(20px, 4vw, 40px); }
@media (max-width: 700px) {
  .fd-app { grid-template-columns: minmax(0, 1fr); }
  .fd-nav { display: flex; flex-wrap: wrap; gap: 8px; padding: 12px 16px; border-right: 0; border-bottom: 1px solid var(--fd-line-app); }
}
```

## Choosing controls

| Task | Preferred approach |
| --- | --- |
| Pick one of several options | Radio cards with previews and short names |
| Set an approximate amount | Slider with the result; an exact field when precision matters |
| Show relations between objects | Diagram with direct manipulation and an equivalent through selection or buttons |
| Upload an image | Drop zone, an accessible file picker button and a preview |
| Understand the effect of a setting | Before and after, or a live preview |
| Enter a name, address or search | A plain labeled field, an interactive layer does not help here |
| Open a rare option | Details or another simple disclosure instead of a permanent panel |

First remove unnecessary decisions, then improve the controls for the ones left. Do not add a complex diagram for decoration.
