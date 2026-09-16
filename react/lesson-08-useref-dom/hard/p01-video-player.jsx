/*
LESSON 08 — useRef & DOM Access
HARD P01 — Video Player Controls
============================================
CONCEPT: Media elements are imperative — `.play()`, `.pause()`, `.currentTime` — so a ref on `<video>` is the natural way to drive them from React.
PROBLEM: Build a `VideoPlayer` with `videoRef` and `playing` state. `togglePlay` calls `videoRef.current.play()`/`.pause()` and flips state; `seek(t)` sets `currentTime`. Render a `<video ref={videoRef}>` plus Play/Pause, Restart, and +10s buttons.
TRY THIS: Render `<VideoPlayer />`, press Play, then +10s, then Pause.
EXPECTED OUTPUT: Video plays, jumps forward 10 seconds, and pauses — all via the ref.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
