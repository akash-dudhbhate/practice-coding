# E-commerce Product Page (React) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-08-ecommerce-product-page/
├── src/App.jsx, src/components/ProductGallery.jsx, src/components/ProductInfo.jsx, src/components/SizeSelector.jsx, src/components/Reviews.jsx, src/components/AddToCart.jsx
└── README.md
```

---

## Implementation Steps

### Step 1: Product Data

Create product object: images[], name, price, description, sizes[], reviews[].

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: ProductGallery

Main image + thumbnails. Click thumbnail to change main. Zoom on hover.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: ProductInfo

Name, price, description, rating stars, stock status.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: SizeSelector

Size buttons. Selected state. Out-of-stock sizes disabled.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: QuantitySelector

+/- buttons. Min 1, max stock. Input field.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: AddToCart

Button with loading state. Toast notification on add. Cart count badge.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Reviews

List of reviews with rating, author, date, comment. Rating summary.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Styling

Two-column layout (gallery + info). Responsive: stacks on mobile.

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] Image gallery with thumbnails
- [ ] Product info (name, price, description)
- [ ] Size selector with states
- [ ] Quantity selector
- [ ] Add to cart with notification
- [ ] Reviews section with ratings
- [ ] Responsive (2-col → 1-col)
- [ ] Loading states

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
