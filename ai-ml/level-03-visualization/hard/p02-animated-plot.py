"""
LEVEL 03 — Data Visualization
HARD P02 — Animated Plot
========================================

CONCEPT:
  matplotlib.animation.FuncAnimation updates a plot each frame:
    anim = FuncAnimation(fig, update_func, frames=N, interval=ms)
  Inside update(frame): change the line's data, return the artists.

PROBLEM:
  Write `animate()` that:
    1. x = linspace(0, 2π, 100); line = plot sin(x)
    2. update(frame) shifts phase: sin(x + frame/10)
    3. FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    4. Show it, return the x array

TRY THIS INPUT:
  ```python
  x = animate()
  print(len(x))                # 100
  print(f"{x[-1]:.4f}")        # 6.2832 (2π)
  ```

EXPECTED OUTPUT:
  ```
  100
  6.2832
  ```
  (plus an animated sine wave window)

HINT:
  def update(frame):
      line.set_ydata(np.sin(x + frame / 10))
      return line,

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# x = animate()
# print(len(x))
