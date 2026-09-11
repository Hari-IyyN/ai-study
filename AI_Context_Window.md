# AI & LLM Fundamentals – Context Window

## 1. Context Window

- Maximum amount of information an LLM can consider in a single request.
- Measured in **tokens**.
- Can include instructions, chat history, user input, RAG content, and tool results.

**Hint:** Context window = the model's temporary working space.

## 2. What Goes Inside the Context?

- System instructions
- Developer instructions
- User message
- Previous conversation/history
- RAG retrieved content
- Tool/function results
- Other application context

**Flow:** `Instructions + History + User Input + RAG/Tools → Context Window → LLM → Response`

## 3. Context Window vs Output Token Limit



### Context Window

- Overall token space available for a request.



### Output Token Limit

- Maximum tokens the model can generate in its response.

**Simple:** Context window = overall space; output limit = response generation space.

