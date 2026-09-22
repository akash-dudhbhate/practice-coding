/*
LESSON 08 — useRef & DOM Access
MEDIUM P03 — CustomInput with forwardRef
============================================
CONCEPT: Function components can't take `ref` directly — `forwardRef((props, ref) => ...)` forwards it to the real DOM node inside.
PROBLEM: Build `CustomInput = forwardRef((props, ref) => <input ref={ref} {...props} style={...} />)`, then a `Parent` component whose button focuses the CustomInput through its own `inputRef`. Export `Parent` as default.
TRY THIS: Render `<Parent />` and click "Focus Custom Input".
EXPECTED OUTPUT: Focus lands inside the styled custom input.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
