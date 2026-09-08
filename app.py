# from openai import OpenAI

# client = OpenAI()

# question = input("What is your question? ")

# response = client.responses.create(
#     model="gpt-5.2",
#     input=question
# )

# print("\nAI Response:")
# print(response.output_text)



from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

question = input("What is your question? ")

response = client.responses.create(
    model="nvidia/nemotron-3.5-lightning:free",
    input=question,
)

print("\nAI Response:")
print(response.output_text)


