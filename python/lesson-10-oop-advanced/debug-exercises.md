# Lesson 10 — Debug Exercises

## Debug 01 (Easy): Missing super().__init__()
```python
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        self.num_doors = num_doors
```
<details><summary>Answer</summary>
**Bug:** Parent's `__init__` not called — `make`, `model`, `year` never set.
**Fix:** `super().__init__(make, model, year); self.num_doors = num_doors`.
</details>

## Debug 02 (Medium): Property without setter
```python
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @property
    def area(self):
        return self.w * self.h

r = Rectangle(4, 5)
r.area = 20
```
<details><summary>Answer</summary>
**Bug:** `@property` without `@area.setter` makes area read-only. `r.area = 20` → AttributeError.
**Fix:** Remove the assignment (area is computed) or add a setter.
</details>

## Debug 03 (Hard): Wrong MRO
```python
class A:
    def speak(self): return "A"
class B(A):
    def speak(self): return "B"
class C(A):
    def speak(self): return "C"
class D(B, C):
    pass
D().speak()
```
<details><summary>Answer</summary>
Returns `"B"` — MRO (Method Resolution Order) is D → B → C → A. Python uses C3 linearization. `D().speak()` finds `B.speak()` first.
</details>
