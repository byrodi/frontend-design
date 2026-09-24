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
| Warning | `#b86e00` | Amber line or icon of a caution, not a text color |
| Error | `#a8324b` | Line, outlined button and short text of a failure or a danger |
| Success | `#267348` | Line and short text of a confirmed result |

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

## Marks of state

Beyond fill and text the family draws state with three devices: a bar on the left edge, a hatch and a dashed frame. Each device carries one meaning, so a reader learns it once and reads it everywhere. The words on the element still say what the state is; the drawing only lets the eye find it.

### Left bar: a notice

A remark stands in the flow of the page as a surface with a thin border and a 4 px bar on its left edge. The color of the bar names the kind:

- deep rose for a plain notice or a beta note;
- error red for a failure or a request that waits for the person's answer, on soft rose when it must be seen first;
- success green for a confirmed result, a delivery, a saved change;
- plum for a remark made by the system: archived, closed as a whole, a draft.

The fill stays the surface or a soft tint, never the semantic color itself. A smaller variant, a 3 px plum bar on soft plum with round outer corners, fits a note inside a panel.

```css
.fd-notice { margin: 0; padding: 12px 16px; border: 1px solid var(--fd-line); border-left: 4px solid var(--fd-rose); border-radius: var(--fd-radius-sm); background: var(--fd-surface); }
.fd-notice--error { border-left-color: var(--fd-error); background: var(--fd-rose-soft); color: var(--fd-error); }
.fd-notice--success { border-left-color: var(--fd-success); }
.fd-notice--system { border-left-color: var(--fd-plum); }
```

### Hatch: exists, but not available

Thin diagonal lines over a soft fill mark space that exists and cannot be used, or an object that will not happen. It is one repeating gradient: a 1-2 px line every 6-10 px, one step darker than the fill, on an opaque background, so the text on it keeps 4.5:1 and nothing shows through. Lowering the opacity instead is not the same thing; it makes the text unreadable and the layers bleed. The pair of fill and line tells the kind:

- neutral: app background and the site border line, for closed hours, breaks and time that is gone; the canvas says "not here" without a word;
- grey on a card: a muted line on the app background, a thin grey edge and the title struck through, for a cancelled or declined object; it stays in place so the history is visible and sinks under live cards;
- tinted: blush lines on soft plum, for a block the person made on purpose, such as a reserved slot or a special element worth a glance.

Turn the angle between the background and the cards (135deg behind, 45deg on a card), so a hatched card stays visible on hatched time. Two or three hatch colors on one screen are fine as long as each keeps its meaning; a hatch as pure decoration is not.

```css
.fd-hatch { background-color: var(--fd-bg-app); background-image: repeating-linear-gradient(135deg, transparent 0 6px, var(--fd-line) 6px 8px); }
.fd-hatch--card { border: 1px solid var(--fd-control-line); background-image: repeating-linear-gradient(45deg, transparent 0 6px, color-mix(in srgb, var(--fd-muted) 12%, var(--fd-bg-app)) 6px 7px); color: var(--fd-muted); }
.fd-hatch--special { background-color: var(--fd-plum-soft); background-image: repeating-linear-gradient(135deg, transparent 0 6px, var(--fd-brand-blush) 6px 8px); }
.fd-hatch--card .fd-hatch__title { text-decoration: line-through; text-decoration-thickness: 1.5px; }
```

### Dashed frame: not final, take care

A dashed border means the object is not settled, or the action inside deserves a second look. The color keeps its meaning from the palette:

- 2 px dashed plum text color: a request or a proposal waiting for an answer;
- 2 px dashed deep rose: changed on the page and not saved yet, with the words "not saved" on it;
- 2 px dashed amber: a caution zone, an action that is reversible but disruptive, such as leaving everywhere or resetting;
- 2 px dashed error red: a danger zone with an irreversible action; its button is outlined in the same red, never a filled red button next to the pink primary one;
- 1 px dashed control line on the app background: a ghost, the old place of a dragged object or an empty placeholder.

A frame is 2 px where the neighbouring sections have 1 px, so the padding gives back 1 px and the content lines up. Frame only what needs it: one caution and one danger zone per screen at most; when everything is framed, nothing is.

```css
.fd-zone { padding: 15px; border: 2px dashed var(--fd-warning); border-radius: var(--fd-radius-lg); background: var(--fd-surface); }
.fd-zone--danger { border-color: var(--fd-error); }
.fd-zone--danger .fd-button { border-color: var(--fd-error); color: var(--fd-error); }
.fd-ghost { border: 1px dashed var(--fd-control-line); background: var(--fd-bg-app); color: var(--fd-muted); }
```

### Amber and red

Amber `--fd-warning` says "attention": a line, an icon, a dashed frame. It reaches 3:1 on every surface of the family and no more, so it is never small text. Error red `--fd-error` says "danger" or "failed": a line, an outlined button, a short sentence. Neither one fills a large area. The page stays white and pink, and the color appears on the edge of what it marks.

### Pink and plum side by side

The two accents work as two branches of state on one screen, not as decoration. Pink is live and ahead: soft rose fill, a rose bar on the left, main text. Plum is finished or made by the system: soft plum fill, a thin line, muted text. On a schedule this gives pink for what is coming and plum for what is behind, readable at a glance with no legend. The bar grows with certainty: 3 px rose for a plain object, 5 px dark rose for a confirmed one. A dashed frame or a hatch replaces the bar when the object is not settled or will not happen.

| State | Fill | Edge | Text |
| --- | --- | --- | --- |
| Upcoming | Soft rose | 3 px rose bar on the left | Main text |
| Confirmed | Soft rose | 5 px dark rose bar, a check icon | Main text |
| Waiting for an answer | Surface | 2 px dashed plum, a clock icon | Main text |
| Not saved | Surface | 2 px dashed deep rose | "not saved" in dark rose |
| Finished or missed | Soft plum | 1 px site border | Muted, the outcome in words |
| Cancelled or declined | Grey hatch at 45deg | 1 px control line, dashed if declined | Muted, title struck through |

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
