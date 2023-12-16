# Import libraries
import openai

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def llm_response(user_input, context=None):
    # Use GPT-like model to generate responses
    response = openai.Completion.create(
        engine="text-davinci-002",  # Adjust as needed
        prompt=user_input,
        max_tokens=150,
        temperature=0.7,
        stop=None  # Can be used to customize stopping criteria
    )
    return response.choices[0].text.strip()