# Lesson 08 — Concepts Explained (CSS Text & Typography)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## font-family

**What:** `font-family` sets the typeface for text. You provide a list of fonts (a "font stack") — the browser uses the first one available.

```css
body {
  font-family: "Helvetica Neue", Arial, sans-serif;
}
```

- `"Helvetica Neue"` — tried first (quoted because it has a space).
- `Arial` — fallback if Helvetica Neue isn't available.
- `sans-serif` — final fallback (the browser's default sans-serif font).

Generic families: `serif` (Times), `sans-serif` (Helvetica/Arial), `monospace` (Courier), `cursive`, `fantasy`.

**Why it exists:** Different fonts convey different tones — serif for formal/traditional, sans-serif for modern/clean, monospace for code. The font stack ensures text always renders even if the user doesn't have your preferred font.

**Where it's used:** Every text element on every website. Set a base font on `body` and let elements inherit it.

**What goes wrong without it:**
- Using a font the user doesn't have with no fallback → browser uses its default (usually Times New Roman), looks unprofessional.
- Forgetting quotes on multi-word font names (`Helvetica Neue` without quotes) → browser doesn't recognize it.
- Using too many fonts (3+) → slow page load, visual clutter. Stick to 1-2 font families.

---

## font-size

**What:** `font-size` sets the size of text. Units: `px` (pixels), `rem` (root em), `em` (relative to parent), `%`.

```css
body { font-size: 16px; }      /* base size */
h1 { font-size: 2rem; }        /* 2 × 16px = 32px (relative to root) */
p { font-size: 1em; }          /* 1 × parent's font-size */
.small { font-size: 0.875rem; } /* 14px */
```

- `px` — fixed, predictable, but doesn't scale with user preferences.
- `rem` — relative to the root (`<html>`) font-size. Scales with user's browser font settings. **Preferred for accessibility.**
- `em` — relative to the PARENT's font-size. Compounds when nested (1em inside 1em = 1× parent, which is already 1× its parent).

**Why it exists:** Text needs different sizes for hierarchy — big headings, small captions. `rem` respects user accessibility settings (users who increase browser font size get bigger text).

**Where it's used:** Headings, body text, captions, buttons, labels — every text element.

**What goes wrong without it:**
- Using `px` everywhere → users who set larger browser font sizes don't get bigger text (accessibility failure).
- `em` in nested elements → sizes compound unpredictably (1.2em inside 1.2em = 1.44× root, not 1.2×).
- No size hierarchy → everything is the same size, no visual structure.
- Too small text (< 14px) → hard to read, fails accessibility.

---

## line-height

**What:** `line-height` controls the vertical space between lines of text. It's the height of each line box.

```css
p { line-height: 1.5; }    /* 1.5× the font-size — good for readability */
p { line-height: 24px; }   /* fixed 24px */
p { line-height: 1.5em; }  /* 1.5× font-size */
```

- Unitless `1.5` is preferred — it's relative to the element's own font-size and inherits cleanly.
- `1` = text touches (too tight). `1.5` = comfortable for body text. `2` = very loose (headings sometimes).

**Why it exists:** Default line-height (~1.2) is too tight for paragraphs — lines blur together. Proper line-height makes text scannable and readable, especially for long content.

**Where it's used:** Body text (1.5-1.6), headings (1.2-1.3), buttons/UI (1 or tight), code blocks (1.4-1.5).

**What goes wrong without it:**
- `line-height: 1` → lines of text touch, hard to read, looks cramped.
- `line-height: 3` → too much space, text looks disconnected, wastes vertical space.
- Using `px` line-height → doesn't scale when font-size changes. Use unitless (e.g. `1.5`).
- Forgetting line-height on body text → default (~1.2) is too tight for paragraphs.

---

## text-align

**What:** `text-align` controls horizontal alignment of text within an element.

```css
h1 { text-align: center; }     /* centered */
p { text-align: left; }        /* left (default for LTR) }
.date { text-align: right; }   /* right-aligned }
.justified { text-align: justify; }  /* stretched to fill width */
```

Values: `left`, `right`, `center`, `justify`.

**Why it exists:** Different content needs different alignment — centered headings, right-aligned dates, justified articles. Text alignment is fundamental to document layout.

**Where it's used:** Headings (centered), table columns (right-aligned numbers), dates/prices (right), article body (left or justified).

**What goes wrong without it:**
- `text-align: center` on long paragraphs → hard to read (ragged center, no clear left edge).
- `text-align: justify` without hyphenation → large gaps between words ("rivers of white space").
- `text-align: right` for LTR reading → unnatural reading flow.
- Confusing `text-align` with flexbox `justify-content` → `text-align` aligns TEXT inside an element; `justify-content` aligns flex CHILDREN.

---

## color

**What:** `color` sets the text color. It accepts named colors, hex, rgb, hsl.

```css
h1 { color: #333333; }          /* hex — dark gray */
p { color: rgb(51, 51, 51); }   /* rgb — same dark gray */
a { color: #0066cc; }           /* hex — blue */
.error { color: red; }          /* named color */
```

**Why it exists:** Color conveys meaning — blue links, red errors, gray secondary text. It's also critical for contrast/accessibility.

**Where it's used:** Every text element. Also inherited — set on `body`, children inherit it.

**What goes wrong without it:**
- Low contrast (light gray on white) → unreadable, fails WCAG (need 4.5:1 ratio).
- Relying on color alone for meaning → colorblind users miss it (e.g. red error text with no icon).
- `color` is inherited → setting it on a parent affects all children unless overridden. Forgetting this leads to unexpected colors.

---

## font-weight and font-style

**What:** `font-weight` controls boldness; `font-style` controls italic.

```css
h1 { font-weight: 700; }    /* bold */
p { font-weight: 400; }     /* normal */
strong { font-weight: 700; }
em { font-style: italic; }
.caption { font-style: italic; font-weight: 300; }  /* light italic */
```

- `font-weight`: 100 (thin), 300 (light), 400 (normal), 500 (medium), 700 (bold), 900 (black).
- `font-style`: `normal`, `italic`, `oblique`.
- The font must HAVE the weight installed — `font-weight: 300` only works if the font has a light variant.

**Why it exists:** Bold and italic create emphasis and hierarchy without changing size. Bold for important text, italic for emphasis/quotes/captions.

**Where it's used:** Headings (bold), emphasis (`<strong>`, `<em>`), captions (italic), button labels (medium/bold).

**What goes wrong without it:**
- `font-weight: 700` on a font that only has 400 → browser "fakes" bold (synthetic bold), looks blurry.
- Using `<b>` for emphasis instead of `font-weight` → `<b>` is semantic (no meaning), `<strong>` means "important." Use CSS for styling, semantic tags for meaning.
- Forgetting that `font-style: italic` needs an italic font variant → browser slants the normal font (fake italic), looks off.

---

## text-decoration

**What:** `text-decoration` adds lines to text: underline, overline, line-through.

```css
a { text-decoration: underline; }       /* underlined links */
a { text-decoration: none; }            /* remove underline */
.done { text-decoration: line-through; } /* strikethrough */
h1 { text-decoration: underline; text-decoration-color: red; }
```

- `text-decoration: none` removes underlines (common for nav links).
- `text-decoration: line-through` for deleted/completed items.
- `text-decoration-color` and `text-decoration-style` customize the line.

**Why it exists:** Underlines are the standard visual cue for links. Strikethrough shows deleted/completed text. Controlling this is essential for link styling.

**Where it's used:** Links (underline or remove), completed tasks (strikethrough), headings (decorative underlines).

**What goes wrong without it:**
- Removing underline from links without another cue → users don't know it's a link. Always provide color + hover state or keep the underline.
- `text-decoration: none` on body text that's actually a link → accessibility issue; links must be distinguishable.
- Forgetting `text-decoration: none` on nav links → they're underlined by default, looks cluttered.

---

## letter-spacing and text-transform

**What:** `letter-spacing` controls space between characters. `text-transform` changes text casing.

```css
h1 { letter-spacing: 2px; }        /* wider letters */
.caps { text-transform: uppercase; }  /* ALL CAPS */
.lower { text-transform: lowercase; }  /* all lowercase */
.title { text-transform: capitalize; } /* Every Word Capitalized */
```

**Why it exists:** Letter-spacing improves readability for all-caps text (which is otherwise cramped). Text-transform changes appearance without changing the underlying HTML text (good for consistency — the source stays "hello" but displays "HELLO").

**Where it's used:** Headings/buttons in uppercase (with letter-spacing), labels, badges, navigation.

**What goes wrong without it:**
- Uppercase text without letter-spacing → letters cramped, hard to read.
- `text-transform: uppercase` on long paragraphs → SHOUTING, hard to read. Use for short labels only.
- Using `text-transform` and also typing the text in uppercase in HTML → double transformation, source is harder to edit. Type normally, transform with CSS.

---

## text-shadow

**What:** `text-shadow` adds a shadow behind text.

```css
h1 {
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  /* offset-x, offset-y, blur-radius, color */
}

.glow {
  text-shadow: 0 0 10px rgba(0, 200, 255, 0.8);  /* glow effect */
}
```

**Why it exists:** Shadows add depth and can improve text readability over images (a dark shadow behind light text on a photo).

**Where it's used:** Hero text over images, decorative headings, glowing/neon effects.

**What goes wrong without it:**
- Heavy shadows on body text → reduces readability, looks amateurish.
- Text over images without shadow or background → invisible in some areas (light text on light part of image).
- Too much blur → muddy, unclear shadow. Keep it subtle.
