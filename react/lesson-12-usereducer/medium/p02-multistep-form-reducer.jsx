/*
LESSON 12 — useReducer
MEDIUM P02 — Multi-Step Form Reducer
============================================
CONCEPT: Wizard forms have interdependent state (step + collected data + errors). A single reducer keeps transitions explicit: NEXT_STEP, PREV_STEP, UPDATE_FIELD, SET_ERROR.
PROBLEM: Build a `MultiStepForm` using `useReducer(reducer, {step: 1, formData: {name: "", email: ""}, errors: {}})`. The reducer handles `"NEXT_STEP"` (step+1), `"PREV_STEP"` (step-1, min 1), `"UPDATE_FIELD"` (merge `{[action.field]: action.value}` into `formData`), and `"SET_ERROR"`. Render `state.step`, a Name input on step 1, an Email input on step 2, a summary on step 3 — all inputs dispatch `UPDATE_FIELD` — plus Back/Next buttons.
TRY THIS: Render `<MultiStepForm />`, fill Name, click Next twice.
EXPECTED OUTPUT: Step indicator advances; step 3 shows the entered name and email.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
