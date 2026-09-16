"""
LEVEL 14 PROJECT — Multi-Turn Chatbot with History
====================================================

Build a chatbot that remembers the conversation — the thing
every LLM app needs but most tutorials skip.

BUILD class `Chatbot`:
  - __init__(system_prompt): stores the system prompt + empty history
  - chat(user_msg): appends user msg → builds full prompt from
    history → calls llm.chat() → appends reply → returns reply
  - history: list of {"role": "user"/"assistant", "content": str}

The PROMPT should include previous turns so the model has context:
    "System: {system}\nUser: hi\nAssistant: hello\nUser: {current}"

INPUT:
  bot = Chatbot("You are a helpful coding tutor")
  print(bot.chat("what is a function?"))
  print(bot.chat("show me an example"))   # should reference "function"
  print(len(bot.history))                 # 4 entries

EXPECTED OUTPUT:
  ```
  [simulated-llm] Response to: ...function...
  [simulated-llm] Response to: ...example...
  4
  ```

WHY: LLMs are stateless — every call is independent. Multi-turn
  = YOUR job to send history. This is exactly how ChatGPT works.

BONUS: add `.reset()` to clear history.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from llm import chat


class Chatbot:
    def __init__(self, system_prompt):
        # TODO
        pass

    def chat(self, user_msg):
        # TODO
        pass

    def reset(self):
        # TODO: clear history
        pass


if __name__ == "__main__":
    bot = Chatbot("You are a helpful coding tutor")
    print(bot.chat("what is a function?"))
    print(bot.chat("show me an example"))
    print(f"History: {len(bot.history)} turns")
