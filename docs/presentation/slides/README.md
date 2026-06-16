# Slides — "From `if` to `match`"

Self-contained **reveal.js** deck for the workshop's cross-language intro (≈3 min).
Fully offline — no internet needed at showtime.

## Present
- **Double-click `index.html`** — opens in your browser. That's it.
- For the most reliable rendering, serve it instead:
  ```bash
  cd docs/presentation/slides
  python3 -m http.server 8000
  # open http://localhost:8000
  ```

## Keys
| Key | Action |
|-----|--------|
| `→` / `Space` | advance (reveals each step, then next slide) |
| `←` | back |
| `S` | **speaker notes** — your `**Say:**` lines in a presenter window (allow the popup if asked) |
| `F` | fullscreen |
| `O` | slide overview |
| `B` / `.` | blank the screen (pause) |

## What's in here
- `index.html` — the deck (12 slides). Edit this to change content.
- `reveal/` — vendored **reveal.js 5.2.1** (MIT license), pulled from jsDelivr.
  Offline; safe to commit to the repo.
  - `reveal.js`, `reveal.css`, `reset.css`, `theme/black.css`
  - `plugin/highlight/` — syntax highlighting + monokai code theme
  - `plugin/notes/` — the speaker-notes presenter view

## Editing slides
Each slide is a `<section>` in `index.html`.

- **Code blocks:** `<pre><code class="language-python" data-trim data-line-numbers>` —
  change `language-python` / `language-javascript` as needed.
- **Step-by-step reveals:** add `class="fragment"` to any `<p>` — it appears on the
  next key press (used for the fall-through "footgun" reveal and the three Python breaks).
- **Speaker notes:** put your talking points in `<aside class="notes">…</aside>` inside the section.

## Swap the theme (e.g. for a bright room)
Change the theme `<link>` in `<head>`:
```html
<link rel="stylesheet" href="reveal/theme/white.css" id="theme">
```
The bundled code-highlight theme (monokai) is dark-on-dark; on a light slide theme
you'll likely want a light highlight theme too.
