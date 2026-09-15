# Lesson 20 — Coding Check

## Easy

### p01-solve.py — Prompt comparison
- [ ] Vague prompt written
- [ ] Specific prompt written
- [ ] Format-instruction prompt written
- [ ] All 3 prompts documented
- [ ] Output quality differences explained
- [ ] Clear conclusion: specific > vague

### p02-solve.py — Few-shot sentiment
- [ ] 3 examples in prompt (positive, negative, neutral)
- [ ] 5 new test sentences
- [ ] Prompts printed
- [ ] Expected outputs documented
- [ ] Format is consistent

### p03-solve.py — Chain-of-thought
- [ ] Math problem chosen
- [ ] Direct prompt (no reasoning)
- [ ] Chain-of-thought prompt (step-by-step)
- [ ] Both prompts tested
- [ ] Correctness compared
- [ ] CoT is more reliable

## Medium

### p01-solve.py — Prompt template system
- [ ] 3 templates created (summarize, translate, code review)
- [ ] Placeholders in templates
- [ ] Function to fill templates
- [ ] All 3 templates tested
- [ ] Final prompts printed
- [ ] Templates are reusable

### p02-solve.py — Structured output extractor
- [ ] Prompt extracts name, age, email, phone
- [ ] JSON output format specified
- [ ] 3 different input texts tested
- [ ] JSON parsed successfully
- [ ] All fields present in output
- [ ] Error handling for malformed JSON

### p03-solve.py — Temperature experiment
- [ ] Creative prompt written
- [ ] Temperature 0 tested (3 runs)
- [ ] Temperature 0.5 tested (3 runs)
- [ ] Temperature 1.0 tested (3 runs)
- [ ] Temperature 1.5 tested (3 runs)
- [ ] Variation documented
- [ ] When to use each temperature explained

## Hard

### p01-solve.py — Simple RAG pipeline
- [ ] Knowledge base created (5+ documents)
- [ ] Retrieval function implemented
- [ ] Top 3 documents retrieved per question
- [ ] RAG prompt constructed
- [ ] 5 questions tested
- [ ] Answers grounded in documents
- [ ] "I don't know" for out-of-scope questions

### p02-solve.py — Prompt injection defense
- [ ] System prompt for customer service bot
- [ ] 5 injection attempts created
- [ ] Defenses written in system prompt
- [ ] Each injection tested
- [ ] Success/failure documented
- [ ] Defenses improved based on results
- [ ] Summary of what works

### p03-solve.py — Complete LLM application
- [ ] System prompt defined
- [ ] Conversation history tracked (last 5 messages)
- [ ] Temperature control (user can set)
- [ ] Token usage tracked
- [ ] Error handling (timeouts, rate limits)
- [ ] Mock mode (no API key needed)
- [ ] 5-turn conversation tested
- [ ] Canned responses for mock mode
- [ ] Application is functional
