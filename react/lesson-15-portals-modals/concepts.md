# Lesson 15 — Concepts Explained (Portals & Modals)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## The Z-Index Stacking Problem

**What:** CSS `z-index` only works within the same stacking context. A child cannot escape its parent's stacking context, no matter how high its z-index.

```jsx
// Problem: Modal inside a parent with overflow:hidden or transform
function App() {
    return (
        <div style={{ transform: 'translateX(0)', overflow: 'hidden' }}>
            <Modal />  {/* Modal can't escape this div's stacking context */}
        </div>
    );
}

// Modal with z-index: 9999 → still trapped inside the parent
// Because `transform` creates a new stacking context
```

**Why it exists:** CSS stacking contexts are created by: `transform`, `filter`, `opacity < 1`, `position: fixed/sticky`, `z-index` with `position`. Once a parent creates a stacking context, children are trapped → modals, tooltips, and dropdowns can't overlay the rest of the page.

**Where it's used:** Modals, tooltips, dropdowns, notifications — any UI that needs to overlay everything else.

**What goes wrong without it:**
- Modal inside a `transform`-ed parent → modal appears behind other elements → broken UI.
- `overflow: hidden` on a parent → modal gets clipped → can't see the full modal.
- Fighting with z-index values → 9999, 99999, 999999 → still doesn't work → frustration.

---

## createPortal

**What:** `createPortal` renders children into a DOM node outside the current component's tree — usually `document.body`.

```jsx
import { createPortal } from 'react-dom';

function Modal({ children, isOpen }) {
    if (!isOpen) return null;

    return createPortal(
        <div className="modal-overlay">
            <div className="modal-content">
                {children}
            </div>
        </div>,
        document.body  // render here, not in the parent's DOM
    );
}

// Usage
function App() {
    const [isOpen, setIsOpen] = useState(false);
    return (
        <div style={{ transform: 'scale(1)', overflow: 'hidden' }}>
            <button onClick={() => setIsOpen(true)}>Open Modal</button>
            <Modal isOpen={isOpen}>
                <h2>Hello from Modal!</h2>
                <button onClick={() => setIsOpen(false)}>Close</button>
            </Modal>
        </div>
    );
}
// Modal renders in document.body → escapes the parent's stacking context
```

**Why it exists:** Without portals, modals are trapped in their parent's DOM → z-index and overflow issues. Portals teleport the modal to `document.body` → escapes all stacking contexts → always on top.

**Where it's used:** Modals, tooltips, dropdown menus, notifications, popovers, any overlay that must appear above everything.

**What goes wrong without it:**
- Portal to a non-existent node → error. Ensure `document.body` exists (it always does in the browser).
- Portal content is still in the React tree (events bubble up) but in a different DOM location → event delegation works, but CSS inheritance doesn't.
- SSR (Next.js): `document` is not available during server render → wrap in `useEffect` or check `typeof window`.

---

## Event Bubbling through Portals

**What:** Even though a portal is in a different DOM location, React events bubble through the React tree (not the DOM tree).

```jsx
function App() {
    const handleAppClick = () => console.log("App clicked");

    return (
        <div onClick={handleAppClick}>
            <p>Click me or the modal</p>
            <Modal>
                <button>Click me in modal</button>
                {/* Clicking this → "App clicked" still fires! */}
                {/* Because React events follow the React tree, not DOM tree */}
            </Modal>
        </div>
    );
}
```

**Why it exists:** Portals change the DOM location but not the React tree location. React's synthetic event system follows the React tree → events from portal children bubble to React ancestors, even though they're in a different DOM branch.

**Where it's used:** Event delegation, click-outside detection, keyboard handling — all work naturally with portals.

**What goes wrong without it:**
- Assuming portal events don't bubble to parent → wrong. They do bubble (in React's synthetic system).
- Click-outside detection: clicking inside the modal might trigger the parent's click handler → unexpected. Use `stopPropagation` or check `e.target`.
- Native DOM events (addEventListener) follow the DOM tree, not React tree → different behavior. Be aware of the difference.

---

## Building a Modal Component

**What:** A complete modal with overlay, content, close button, and escape key handling.

```jsx
import { createPortal } from 'react-dom';
import { useEffect } from 'react';

function Modal({ isOpen, onClose, children, title }) {
    useEffect(() => {
        if (!isOpen) return;

        const handleEscape = (e) => {
            if (e.key === 'Escape') onClose();
        };

        document.addEventListener('keydown', handleEscape);
        document.body.style.overflow = 'hidden';  // prevent background scroll

        return () => {
            document.removeEventListener('keydown', handleEscape);
            document.body.style.overflow = '';  // restore scroll
        };
    }, [isOpen, onClose]);

    if (!isOpen) return null;

    return createPortal(
        <div className="modal-overlay" onClick={onClose}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                <header>
                    <h2>{title}</h2>
                    <button onClick={onClose}>×</button>
                </header>
                <main>{children}</main>
            </div>
        </div>,
        document.body
    );
}
```

**Why it exists:** A good modal needs: overlay click to close, escape key to close, prevent body scroll, stop propagation on content clicks. Without these, the modal is frustrating to use.

**Where it's used:** Every modal in a React app — confirmation dialogs, forms, image lightboxes, settings panels.

**What goes wrong without it:**
- No `stopPropagation` on content → clicking inside the modal closes it (overlay click fires).
- No body scroll lock → background scrolls when interacting with modal → bad UX.
- No escape key → user must find the close button → accessibility issue.
- No cleanup → body scroll stays locked after modal closes → page is broken.

---

## Accessibility for Modals

**What:** Modals need proper accessibility: focus trap, ARIA attributes, keyboard navigation.

```jsx
function Modal({ isOpen, onClose, children, title }) {
    const modalRef = useRef(null);

    useEffect(() => {
        if (!isOpen) return;

        // Store the element that had focus before opening
        const previouslyFocused = document.activeElement;

        // Focus the modal
        modalRef.current?.focus();

        // Focus trap: keep focus inside modal
        const handleTab = (e) => {
            if (e.key !== 'Tab') return;
            const focusable = modalRef.current?.querySelectorAll(
                'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
            );
            if (!focusable) return;
            const first = focusable[0];
            const last = focusable[focusable.length - 1];
            if (e.shiftKey && document.activeElement === first) {
                e.preventDefault();
                last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
                e.preventDefault();
                first.focus();
            }
        };

        document.addEventListener('keydown', handleTab);
        return () => {
            document.removeEventListener('keydown', handleTab);
            previouslyFocused?.focus();  // restore focus
        };
    }, [isOpen]);

    if (!isOpen) return null;

    return createPortal(
        <div className="modal-overlay" onClick={onClose}>
            <div
                className="modal-content"
                onClick={(e) => e.stopPropagation()}
                ref={modalRef}
                role="dialog"
                aria-modal="true"
                aria-labelledby="modal-title"
                tabIndex={-1}
            >
                <h2 id="modal-title">{title}</h2>
                {children}
            </div>
        </div>,
        document.body
    );
}
```

**Why it exists:** Without accessibility, screen reader users can't navigate the modal, keyboard users tab out of the modal into the background, and focus is lost when the modal closes. Proper ARIA and focus management make modals usable for everyone.

**Where it's used:** Every production-quality modal — required for WCAG compliance.

**What goes wrong without it:**
- No focus trap → Tab key moves focus to background elements → confusing for keyboard users.
- No focus restore → after closing, focus goes to `<body>` → user loses their place.
- Missing `aria-modal="true"` → screen readers don't announce the modal → users don't know it's there.

---

## Tooltips with Portals

**What:** Portals are also useful for tooltips that might be clipped by parent overflow.

```jsx
function Tooltip({ children, content }) {
    const [isVisible, setIsVisible] = useState(false);
    const [position, setPosition] = useState({ top: 0, left: 0 });
    const targetRef = useRef(null);

    const showTooltip = () => {
        const rect = targetRef.current.getBoundingClientRect();
        setPosition({
            top: rect.bottom + window.scrollY + 8,
            left: rect.left + window.scrollX,
        });
        setIsVisible(true);
    };

    return (
        <>
            <span
                ref={targetRef}
                onMouseEnter={showTooltip}
                onMouseLeave={() => setIsVisible(false)}
            >
                {children}
            </span>
            {isVisible && createPortal(
                <div className="tooltip" style={{ position: 'absolute', ...position }}>
                    {content}
                </div>,
                document.body
            )}
        </>
    );
}
```

**Why it exists:** Tooltips inside a parent with `overflow: hidden` → tooltip is clipped → only part visible. Portals render the tooltip in `document.body` → not clipped → always fully visible.

**Where it's used:** Hover tooltips, info icons, help text, any small overlay that might be clipped.

**What goes wrong without it:**
- Tooltip position relative to viewport → must account for scroll (`window.scrollY`). Forgetting this → tooltip appears in the wrong place when scrolled.
- Tooltip inside `overflow: hidden` without portal → clipped → invisible. Always use portals for tooltips.
- Position calculation on every hover → fine for small tooltips, but for many tooltips, consider a shared tooltip component.

---

## Animations with Portals

**What:** Animate modal enter/exit transitions.

```jsx
function Modal({ isOpen, onClose, children }) {
    const [shouldRender, setShouldRender] = useState(isOpen);

    useEffect(() => {
        if (isOpen) {
            setShouldRender(true);
        } else {
            // Delay unmount for exit animation
            const timer = setTimeout(() => setShouldRender(false), 300);
            return () => clearTimeout(timer);
        }
    }, [isOpen]);

    if (!shouldRender) return null;

    return createPortal(
        <div className={`modal-overlay ${isOpen ? 'fade-in' : 'fade-out'}`} onClick={onClose}>
            <div className={`modal-content ${isOpen ? 'slide-in' : 'slide-out'}`} onClick={e => e.stopPropagation()}>
                {children}
            </div>
        </div>,
        document.body
    );
}

// CSS
// .modal-overlay { transition: opacity 0.3s; }
// .modal-overlay.fade-in { opacity: 1; }
// .modal-overlay.fade-out { opacity: 0; }
```

**Why it exists:** Without exit animations, modals disappear instantly → jarring. Delaying unmount allows the exit animation to play → smooth transitions.

**Where it's used:** Every animated modal, notification, or toast. Libraries like Framer Motion handle this automatically, but understanding the pattern is important.

**What goes wrong without it:**
- Forgetting to delay unmount → modal disappears before exit animation → no animation visible.
- Not cleaning up the timeout → if component unmounts during exit → setState on unmounted component → warning.
- Using `display: none` for hiding → no transition (display is not animatable). Use `opacity` or `transform`.
