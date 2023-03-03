import openai
import os

openai.api_key = os.getenv("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")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()