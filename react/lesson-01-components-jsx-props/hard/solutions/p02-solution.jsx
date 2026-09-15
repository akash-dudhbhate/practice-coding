// Lesson 01 — Hard P02: Nested Comment Tree (recursive)
function Comment({ comment }) {
  return (
    <div style={{ marginLeft: "20px", borderLeft: "2px solid #ddd", paddingLeft: "10px", margin: "8px 0" }}>
      <p><strong>{comment.author}</strong>: {comment.text}</p>
      {comment.replies && comment.replies.map((reply) => (
        <Comment key={reply.id} comment={reply} />
      ))}
    </div>
  );
}
export default Comment;
