# Lesson 04 — Common Mistakes

## Mistake 01: No alt text
```html
<!-- WRONG -->
<img src="photo.jpg">
<!-- CORRECT -->
<img src="photo.jpg" alt="Sunset over mountains">
```

## Mistake 02: Huge images
```html
<!-- WRONG — 5MB image for a 200px thumbnail -->
<img src="huge-photo.jpg" width="200">
<!-- CORRECT — resize on server -->
<img src="thumbnail.jpg" width="200" alt="...">
```

## Mistake 03: No video controls
```html
<!-- WRONG -->
<video src="movie.mp4"></video>
<!-- CORRECT -->
<video src="movie.mp4" controls></video>
```

## Mistake 04: Iframe without title
```html
<!-- WRONG -->
<iframe src="..."></iframe>
<!-- CORRECT -->
<iframe src="..." title="Map"></iframe>
```

## Mistake 05: Not using lazy loading
```html
<!-- WRONG — loads all images immediately -->
<img src="photo.jpg" alt="...">
<!-- CORRECT — loads when needed -->
<img src="photo.jpg" loading="lazy" alt="...">
```
