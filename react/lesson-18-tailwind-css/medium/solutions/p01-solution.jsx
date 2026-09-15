// Lesson 18 — Medium P01: Reusable Button with variants
import { clsx } from "clsx";
const variants = {
  primary: "bg-blue-500 text-white hover:bg-blue-600",
  secondary: "bg-gray-200 text-gray-800 hover:bg-gray-300",
  danger: "bg-red-500 text-white hover:bg-red-600",
};
const sizes = { sm: "px-3 py-1 text-sm", md: "px-4 py-2", lg: "px-6 py-3 text-lg" };
function Button({ variant = "primary", size = "md", className, children, ...props }) {
  return <button className={clsx("rounded transition-colors focus:outline-none focus:ring-2 focus:ring-blue-400", variants[variant], sizes[size], className)} {...props}>{children}</button>;
}
export default Button;
