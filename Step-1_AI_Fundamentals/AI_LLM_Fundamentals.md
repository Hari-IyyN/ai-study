# AI & LLM Fundamentals

## 1. What is AI?

**Artificial Intelligence (AI)** is the technology of building computer systems that can perform tasks that normally require human intelligence.

Examples:

- Understanding language
- Recognizing images
- Making predictions
- Solving problems
- Making decisions
- Learning from data

### Simple idea

> **AI = Making computers perform intelligent tasks.**

---

## 2. What is Generative AI?

**Generative AI** is a type of AI that can **create new content** based on the input it receives.

It can generate:

- Text
- Images
- Audio
- Video
- Code

Examples:

- ChatGPT → generates text
- Image generation models → generate images
- Code generation models → generate code



### Simple idea

> **Generative AI = AI that can create new content.**

---



## 3. What is an LLM?

**LLM = Large Language Model**

An LLM is an AI model specifically designed to understand and generate **human language**.

Examples:

- GPT
- Claude
- Gemini
- Llama
- Mistral

LLMs can:

- Answer questions
- Generate text
- Summarize information
- Translate languages
- Generate code
- Analyze text
- Follow instructions
- Maintain conversational context



### Simple idea

> **LLM = An AI model specialized in understanding and generating language.**

---



# 4. AI vs Generative AI vs LLM

Think of them as a hierarchy:

```text
Artificial Intelligence (AI)
│
├── Traditional / Predictive AI
│
└── Generative AI
    │
    ├── Text Generation
    │   └── LLMs
    │
    ├── Image Generation
    ├── Audio Generation
    └── Video Generation
```

So:

**AI** → The broad field

**Generative AI** → AI that generates new content

**LLM** → A Generative AI model focused primarily on language

---



# 5. How does an LLM basically work?

At a high level:

```text
User Input
    ↓
Tokenization
    ↓
Tokens / Token IDs
    ↓
LLM / Transformer
    ↓
Predict Next Tokens
    ↓
Generated Tokens
    ↓
Text Response
```

For example:

```text
User:
"What is AI?"

        ↓

Tokenizer

        ↓

Token IDs

        ↓

LLM / Transformer

        ↓

Generated Tokens

        ↓

"AI is the field of..."
```

You already studied **Tokens**, so this connects directly with what you learned earlier.

---



# 6. What does "Large" mean in LLM?

**Large** mainly refers to the scale of the model and its training.

It can involve:

- Large amounts of training data
- Large number of model parameters
- Large computational resources
- Large context capabilities

Don't think of "large" as simply meaning the model knows everything.

---



# 7. What is a Model?

A **model** is a trained mathematical system that has learned patterns from data.

For an LLM:

```text
Training Data
      ↓
Training Process
      ↓
Learned Parameters
      ↓
LLM
      ↓
Input
      ↓
Output
```

The model doesn't simply store every sentence like a normal database.

Instead, training allows it to learn **patterns and relationships in data**.

---



# 8. What is a Transformer?

A **Transformer** is a neural network architecture that became the foundation of modern LLMs.

The important paper was:

**"Attention Is All You Need" — 2017**

Transformers introduced the **self-attention mechanism**, which allows the model to determine which parts of the input are important in relation to other parts.

Modern LLMs such as GPT-family models are based on Transformer-related architectures.

### For now, remember:

> **Transformer = Core architecture behind modern LLMs.**

You don't need to study the mathematics of attention yet. We can study that separately later if needed.

---



# 9. Important Terms to Remember


| Term               | Simple Meaning                                                     |
| ------------------ | ------------------------------------------------------------------ |
| **AI**             | Broad field of machine intelligence                                |
| **Generative AI**  | AI that creates new content                                        |
| **LLM**            | Language-focused AI model                                          |
| **Model**          | Trained system that learns patterns                                |
| **Token**          | Small unit of text processed by an LLM                             |
| **Tokenizer**      | Converts text into tokens/token IDs                                |
| **Transformer**    | Architecture used by modern LLMs                                   |
| **Context Window** | Amount of token-based information a model can process in a request |
| **Prompt**         | Instructions/input given to the model                              |




### The main mental model

```text
AI
 ↓
Generative AI
 ↓
LLM
 ↓
Tokenizer
 ↓
Tokens
 ↓
Transformer
 ↓
Generated Tokens
 ↓
Response
```

For our roadmap, **this is enough theory for the first part**. Next, we can go deeper into **how an LLM is trained: Training Data → Pre-training → Parameters → Fine-tuning → Inference**, which is an important foundation before moving further.