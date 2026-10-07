# LangChain Fundamentals

## 1. What is LangChain?

LangChain is an open-source framework for building applications powered
by large language models (LLMs). It provides reusable components for
connecting a model with prompts, tools, data sources, and application
logic.

**Simple idea:** An LLM can answer a prompt. LangChain helps organize
the steps around that model call.

## 2. Why use LangChain?

It can help with prompt construction, model calls, structured output,
tool calling, document retrieval, and multi-step workflows. You do not
need every feature; a simple chatbot may only need a model provider SDK.

## 3. LangChain vs. an SDK

- **Provider SDK:** Sends requests to a model provider.
- **LangChain:** Provides reusable abstractions and integrations for
prompts, models, tools, retrieval, and workflows.
- **LLM:** Generates the response.

LangChain does not replace the model.

## 4. Simple flow

1. User submits a question.
2. The application prepares a prompt.
3. LangChain sends messages to the configured model.
4. The model generates a response.
5. The application returns it to the user.

In RAG, retrieval usually finds relevant context before the model call.

## 5. TypeScript / Node.js example

Install packages:

```bash
npm install @langchain/core @langchain/openai
```

Example using a chat model and prompt template:

```ts
import { ChatOpenAI } from "@langchain/openai";
import { ChatPromptTemplate } from "@langchain/core/prompts";

const model = new ChatOpenAI({
  model: process.env.LLM_MODEL ?? "your-model-name",
  temperature: 0.2,
  apiKey: process.env.LLM_API_KEY,
  // For a compatible provider, configure its supported base URL:
  // configuration: { baseURL: process.env.LLM_BASE_URL },
});

const prompt = ChatPromptTemplate.fromMessages([
  ["system", "You are a helpful assistant. Explain things simply."],
  ["human", "Explain {topic} in three short bullet points."],
]);

const chain = prompt.pipe(model);
const result = await chain.invoke({ topic: "LangChain" });
console.log(result.content);
```

Set `LLM_MODEL`, `LLM_API_KEY`, and---if needed---`LLM_BASE_URL` for
your provider. Keep API keys on the backend, never in frontend code.
Configuration may vary by provider and package version; run this in a
TypeScript-configured backend.

## 6. Where it fits

Typical flow: `Frontend → Backend API → Prompt / workflow → Model`

RAG flow:
`User question → Retrieve relevant chunks → Build prompt with context → Model → Answer`

LangChain can connect these steps, but your app still needs
authentication, authorization, error handling, logging, rate limiting,
and data protection.

## 7. LangChain, LangGraph, and LangSmith

- **LangChain:** Building blocks and integrations for LLM
applications.
- **LangGraph:** Stateful multi-step agent/workflow applications,
branching, and human approval.
- **LangSmith:** Tracing, inspecting, evaluating, and monitoring
application runs.



## 8. Best practices

- Keep API keys on the backend.
- Use clear prompts and validate model output.
- Handle timeouts, rate limits, and provider errors.
- Do not treat model output as automatically true or trusted.
- Limit tool permissions and validate tool inputs.
- Avoid logging unnecessary sensitive data.
- Check current official documentation because APIs and integrations
evolve.



## 9. What to learn next

1. Chat models and message roles
2. Prompt templates and variables
3. Invocation and streaming
4. Structured output
5. Tool calling
6. Embeddings and vector stores
7. Retrieval-Augmented Generation (RAG)
8. LangGraph for complex workflows



## Quick summary

LangChain is a toolkit for connecting LLMs with prompts, tools,
retrieval, and multi-step workflows. Start with a small prompt → model
example and add complexity only when needed.