/*
LESSON 02 — State & useState
HARD P02 — Multi-Step Form
============================================
CONCEPT: A `step` number in state plus `&&` conditional rendering is all you need for a wizard. Each step validates before `setStep(step + 1)` is allowed.
PROBLEM: Build a `MultiStepForm` component. Keep `step` (1-3) and `data` ({ name, email }) state. Step 1 shows the name input, step 2 the email input, step 3 a review. Back/Next buttons appear conditionally; Next refuses to advance while the current field is empty. Step 3 shows a Submit button.
TRY THIS: Render `<MultiStepForm />`, try Next with an empty name, then fill it and walk to step 3.
EXPECTED OUTPUT: Empty field blocks Next; filled fields reach a Review screen with a Submit button.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
