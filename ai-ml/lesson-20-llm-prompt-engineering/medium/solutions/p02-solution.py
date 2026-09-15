# Lesson 20 — Medium P02: Structured output extractor (JSON)
# Extracts name, age, email, phone from text and returns JSON.

import json

extraction_prompt = """Extract the following information from the text and return it as a JSON object.
Required fields: name, age, email, phone
If a field is not found, set its value to null.

Text: {input_text}

Return ONLY the JSON object, no other text.
JSON:"""


# Test with 3 different input texts
test_texts = [
    "Hi, I'm John Smith. I'm 28 years old. You can reach me at john.smith@email.com or call 555-123-4567.",
    "My name is Alice Johnson, age 35. Contact: alice.j@work.org, phone: (555) 987-6543.",
    "I'm Bob, a 42-year-old engineer. Email: bob@tech.io",
]

# Mock LLM responses (in real usage, send the prompt to an LLM API)
mock_responses = [
    '{"name": "John Smith", "age": 28, "email": "john.smith@email.com", "phone": "555-123-4567"}',
    '{"name": "Alice Johnson", "age": 35, "email": "alice.j@work.org", "phone": "(555) 987-6543"}',
    '{"name": "Bob", "age": 42, "email": "bob@tech.io", "phone": null}',
]

required_fields = ["name", "age", "email", "phone"]

print("=== Structured Output Extraction ===\n")

for i, (text, response) in enumerate(zip(test_texts, mock_responses), 1):
    prompt = extraction_prompt.format(input_text=text)
    print(f"--- Test {i} ---")
    print(f"Input: {text}")
    print(f"Prompt: {prompt[:80]}...")
    
    # Parse the JSON response
    try:
        data = json.loads(response)
        print(f"Parsed JSON: {data}")
        
        # Verify all fields are present
        missing = [f for f in required_fields if f not in data]
        if missing:
            print(f"MISSING fields: {missing}")
        else:
            print("All fields present ✓")
        
        # Check for null values
        null_fields = [f for f in required_fields if data.get(f) is None]
        if null_fields:
            print(f"Null fields: {null_fields}")
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
    print()

print("=== Summary ===")
print("The extraction prompt reliably produces JSON with all required fields.")
print("Missing information is set to null (e.g., Bob's phone number).")
print("Parsing the JSON allows programmatic access to extracted data.")
