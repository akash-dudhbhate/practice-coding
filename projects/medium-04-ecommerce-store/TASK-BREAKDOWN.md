# E-commerce Store (React) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-04-ecommerce-store/
├── src/App.jsx, src/pages/Home.jsx, src/pages/ProductDetail.jsx, src/pages/Cart.jsx, src/pages/Checkout.jsx, src/stores/cart.js, src/components/ProductCard.jsx, src/components/Header.jsx
└── README.md
```

---

## Implementation Steps

### Step 1: Router Setup

React Router: /, /product/:id, /cart, /checkout. Layout with header.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Product Data

Mock product data (10+ products): id, name, price, image, category, description, stock.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Home Page

Product grid with filters (category, price range). Sort (price, name). Search.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: ProductCard

Image, name, price, rating. Add to cart button. Hover effect. Link to detail.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: ProductDetail

Gallery, info, quantity selector, add to cart, reviews, related products.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Cart Store

Zustand: items, addItem, removeItem, updateQty, total, clear. localStorage.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Cart Page

List items with qty controls, remove button, subtotal, shipping, total. Checkout button.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Checkout Page

Form: shipping address, payment (mock). Order summary. Place order → success page.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Header

Logo, nav, search, cart icon with count badge. Responsive menu.

**Checkpoint:** Step 9 is complete when the described functionality works.

### Step 10: Responsive

Grid adjusts columns. Cart stacks on mobile. Mobile nav menu.

**Checkpoint:** Step 10 is complete when the described functionality works.

---

## Final Checklist

- [ ] React Router with 4 pages
- [ ] Product grid with filters + sort
- [ ] Product detail page
- [ ] Cart with Zustand store
- [ ] Quantity controls in cart
- [ ] Checkout form (mock)
- [ ] Order success page
- [ ] Header with cart badge
- [ ] Responsive (mobile + desktop)
- [ ] localStorage cart persistence

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
