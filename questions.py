import openai

openai.api_key = 'Your API key'

def ask_question(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    question = response.choices[0].message['content'].strip()
    return question


