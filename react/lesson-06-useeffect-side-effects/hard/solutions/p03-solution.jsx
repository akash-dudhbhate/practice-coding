// Lesson 06 — Hard P03: Multiple Effects Chat
import { useState, useEffect } from "react";
function Chat({ roomId }) {
  const [messages, setMessages] = useState([]);
  const [ws, setWs] = useState(null);
  // Effect 1: Fetch messages on room change
  useEffect(() => {
    setMessages([]);
    fetch(`https://jsonplaceholder.typicode.com/posts?userId=${roomId}`)
      .then((res) => res.json())
      .then((data) => setMessages(data.slice(0, 5).map((d) => d.title)));
  }, [roomId]);
  // Effect 2: Update document title
  useEffect(() => { document.title = `Chat Room ${roomId}`; }, [roomId]);
  // Effect 3: Mock WebSocket
  useEffect(() => {
    const mockWs = { onmessage: null, close: () => console.log("WS closed") };
    setWs(mockWs);
    return () => mockWs.close();
  }, []);
  return (
    <div>
      <h3>Room {roomId}</h3>
      <ul>{messages.map((m, i) => <li key={i}>{m}</li>)}</ul>
    </div>
  );
}
export default Chat;
