# def chatbot_response(user_input):
#     """
#     Generate a response from the chatbot using the OpenAI GPT-like model.

#     Parameters:
#         user_input (str): User's input.

#     Returns:
#         dict: A dictionary containing the chatbot's response and extracted entities.
#     """
#     try:
#         # Use GPT-like model to generate responses
#         response = openai.Completion.create(
#             engine="text-davinci-002",  # Adjust as needed
#             prompt=user_input,
#             max_tokens=150,
#             temperature=0.7,
#             stop=None  # Can be used to customize stopping criteria
#         )
        
#         bot_reply = response.choices[0].text.strip()
#         entities = extract_entities(bot_reply)

#         return {'bot_reply': bot_reply, 'entities': entities}

#     except Exception as e:
#         logger.error(f"Error generating chatbot response: {e}")
#         return {'bot_reply': "An error occurred while processing your request.", 'entities': {}}
