/*
LESSON 13 — React Router
HARD P02 — Multi-Step Wizard with Location State
============================================
CONCEPT: `navigate(path, {state})` can carry data to the next route, read there via `useLocation().state` — letting a wizard accumulate answers across URLs while each step can guard itself ("no name? go back to step 1").
PROBLEM: Build `Step1` (name input; `onBlur` navigates to /wizard/step2 passing `{...location.state, name}` in state; Next link). `Step2` renders "Complete step 1 first" + a link back when `location.state?.name` is missing, else an email input navigating to /wizard/step3 with `{...location.state, email}`. `Step3` guards on `location.state?.email` and shows the collected name + email. `App` maps `/wizard/step1|step2|step3`.
TRY THIS: Render `<App />` and jump straight to /wizard/step3 — it bounces you to step 2. Then complete step 1 → 2 → 3.
EXPECTED OUTPUT: Guards redirect incomplete jumps; step 3 shows "Name: … / Email: …" once both entered.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
