from openai import OpenAI
def aiProcess(command):
    client = OpenAI(
    api_key= "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",
    base_url="https://openrouter.ai/api/v1"
    )

    completion = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis which performs basic tasks like alexa and google cloud.Provide very short and concise answers, no more than 1-2 sentences."},
        {
            "role": "user", "content": command
        }
    ]
    )

    return completion.choices[0].message.content