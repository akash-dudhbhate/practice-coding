/*
LESSON 08 — useRef & DOM Access
HARD P03 — CustomForm with useImperativeHandle
============================================
CONCEPT: useImperativeHandle customizes what a parent's ref can see — expose only `focus/clear/validate/submit` instead of the whole DOM node.
PROBLEM: Build `CustomForm = forwardRef((props, ref) => ...)` wrapping a controlled input; inside, `useImperativeHandle(ref, () => ({ focus, clear, validate, submit }))` using an inner inputRef and value state. Then a `Parent` with `formRef` and four buttons calling each method. Export `Parent` default.
TRY THIS: Render `<Parent />`, type text, click Validate, Clear, Submit.
EXPECTED OUTPUT: Buttons drive the child imperatively: focus moves, text clears, validate/submit act on the value.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
