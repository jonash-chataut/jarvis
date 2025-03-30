from openai import OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= "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"
    )

completion = client.chat.completions.create(
    model="google/gemini-2.0-flash-lite-preview-02-05:free",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis which performs basic tasks like alexa and google cloud.Provide very short and concise answers, no more than 1-2 sentences."},
        {
            "role": "user",
            "content": "who is virat"
        }
    ]
)

print(completion.choices[0].message.content)