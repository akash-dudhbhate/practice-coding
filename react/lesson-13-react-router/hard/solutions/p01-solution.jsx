// Lesson 13 — Hard P01: Blog app with routes
import { BrowserRouter, Routes, Route, Link, useParams } from "react-router-dom";
const posts = [{ slug: "hello-world", title: "Hello World", category: "general" }, { slug: "react-tips", title: "React Tips", category: "tech" }];
function Home() { return <div><h1>Blog</h1>{posts.map((p) => <Link key={p.slug} to={`/post/${p.slug}`}><h3>{p.title}</h3></Link>)}</div>; }
function Post() { const { slug } = useParams(); const post = posts.find((p) => p.slug === slug); return post ? <h1>{post.title}</h1> : <h1>Post not found</h1>; }
function Category() { const { category } = useParams(); const filtered = posts.filter((p) => p.category === category); return <div><h1>Category: {category}</h1>{filtered.map((p) => <Link key={p.slug} to={`/post/${p.slug}`}><h3>{p.title}</h3></Link>)}</div>; }
function Admin() { return <h1>Admin Panel</h1>; }
function NotFound() { return <h1>404</h1>; }
function App() {
  return (
    <BrowserRouter>
      <nav><Link to="/">Home</Link> | <Link to="/category/tech">Tech</Link> | <Link to="/admin">Admin</Link></nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/post/:slug" element={<Post />} />
        <Route path="/category/:category" element={<Category />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
