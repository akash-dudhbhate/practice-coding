# Lesson 20 — Hard P03: Complete LLM chatbot application
# System prompt, conversation history (last 5), temperature control,
# token usage tracking, error handling, mock mode.

import json
from collections import deque


class SimpleChatbot:
    def __init__(self, system_prompt="", temperature=0.7, mock_mode=True):
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.mock_mode = mock_mode
        self.history = deque(maxlen=5)  # Keep last 5 messages
        self.total_tokens = 0

    def _mock_response(self, user_message):
        """Generate a mock response based on user message content."""
        msg = user_message.lower()
        if "hello" in msg or "hi" in msg:
            return "Hello! How can I help you today?"
        elif "how are you" in msg:
            return "I'm doing well, thank you for asking! How can I assist you?"
        elif "weather" in msg:
            return "I don't have access to weather data, but I can help with other questions!"
        elif "joke" in msg:
            return "Why do programmers prefer dark mode? Because light attracts bugs!"
        elif "bye" in msg or "goodbye" in msg:
            return "Goodbye! Have a great day!"
        elif "name" in msg:
            return "I'm a simple chatbot. What's your name?"
        else:
            return f"That's interesting! Tell me more about '{user_message[:30]}...'"

    def _estimate_tokens(self, text):
        """Rough token estimate: ~4 characters per token."""
        return max(1, len(text) // 4)

    def chat(self, user_message):
        """Send a message and get a response."""
        try:
            # Add user message to history
            self.history.append({"role": "user", "content": user_message})
            user_tokens = self._estimate_tokens(user_message)
            self.total_tokens += user_tokens

            # Generate response
            if self.mock_mode:
                response = self._mock_response(user_message)
            else:
                # Real API call would go here
                raise NotImplementedError("Set mock_mode=True or implement API call")

            # Add response to history
            self.history.append({"role": "assistant", "content": response})
            response_tokens = self._estimate_tokens(response)
            self.total_tokens += response_tokens

            return response

        except Exception as e:
            error_msg = f"Error: {str(e)}. Please try again."
            self.history.append({"role": "assistant", "content": error_msg})
            return error_msg

    def get_history(self):
        """Return conversation history."""
        return list(self.history)

    def get_token_usage(self):
        """Return total token usage."""
        return self.total_tokens

    def set_temperature(self, temp):
        """Set temperature (0.0 to 1.5)."""
        self.temperature = max(0.0, min(1.5, temp))

    def clear_history(self):
        """Clear conversation history."""
        self.history.clear()


# Test with a 5-turn conversation
print("=== Chatbot Test (5-turn conversation) ===\n")

bot = SimpleChatbot(
    system_prompt="You are a helpful assistant. Be friendly and concise.",
    temperature=0.7,
    mock_mode=True,
)

conversation = [
    "Hello! How are you?",
    "What's your name?",
    "Tell me a joke!",
    "What's the weather like?",
    "Goodbye!",
]

for msg in conversation:
    print(f"User: {msg}")
    response = bot.chat(msg)
    print(f"Bot:  {response}")
    print(f"Tokens used: {bot.get_token_usage()}\n")

print("=== Conversation History (last 5) ===")
for entry in bot.get_history():
    print(f"  [{entry['role']}] {entry['content']}")

print(f"\nTotal tokens used: {bot.get_token_usage()}")
print(f"Temperature: {bot.temperature}")

# Test error handling
print("\n=== Error Handling Test ===")
bot2 = SimpleChatbot(mock_mode=False)
try:
    resp = bot2.chat("Hello")
    print(f"Response: {resp}")
except Exception as e:
    print(f"Caught error: {e}")
