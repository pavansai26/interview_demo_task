from django.shortcuts import render

# Create your views here.
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from interact_bot.helpers.ner import extract_entities
#from interact_bot.helpers.llm import chatbot_response
#from interact_bot.helpers.user_response import handle_user_response
import openai
import spacy

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'
nlp = spacy.load("en_core_web_sm")



# @api_view(['POST'])
# @csrf_exempt
# def chatbot_api(request):
#     """
#     API endpoint to interact with the chatbot.

#     Parameters:
#         request.data (dict): A dictionary containing user input.

#     Returns:
#         Response: JSON response containing the chatbot's reply.
#     """
#     try:
#         user_input = request.data.get('user_input', '')
#         logger.info(f"Received user input: {user_input}")

#         # Perform named entity recognition
#         entities = extract_entities(user_input)
#         logger.info(f"Extracted entities: {entities}")

#         # Handle user response
#         bot_reply = handle_user_response(user_input)
#         logger.info(f"Generated chatbot reply: {bot_reply}")

#         # Optionally, you can include entities in the response
#         response_data = {
#             'bot_reply': bot_reply,
#             'entities': entities,
#         }

#         logger.info("Returning response to the user")
#         return Response(response_data, status=status.HTTP_200_OK)

#     except Exception as e:
#         logger.error(f"Error processing request: {e}")
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
def chatbot_response(user_input):
    """
    Generate a response from the chatbot using the OpenAI GPT-like model.

    Parameters:
        user_input (str): User's input.

    Returns:
        dict: A dictionary containing the chatbot's response and extracted entities.
    """
    try:
        # Use GPT-like model to generate responses
        response = openai.Completion.create(
            engine="text-davinci-002",  # Adjust as needed
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
            stop=None  # Can be used to customize stopping criteria
        )
        
        bot_reply = response.choices[0].text.strip()
        entities = extract_entities(bot_reply)

        return {'bot_reply': bot_reply, 'entities': entities}

    except Exception as e:
        logger.error(f"Error generating chatbot response: {e}")
        return {'bot_reply': "An error occurred while processing your request.", 'entities': {}}



@api_view(['POST'])
@csrf_exempt
def chatbot_api(request):
    """
    API endpoint to interact with the chatbot.

    Parameters:
        request.data (dict): A dictionary containing user input.

    Returns:
        Response: JSON response containing the chatbot's reply and extracted entities.
    """
    try:
        user_input = request.data.get('user_input', '')
        logger.info(f"Received user input: {user_input}")

        # Generate chatbot response
        response_data = chatbot_response(user_input)
        logger.info(f"Generated chatbot reply: {response_data['bot_reply']}")

        # Optionally, you can include entities in the response
        logger.info("Returning response to the user")
        return Response(response_data, status=status.HTTP_200_OK)

    except Exception as e:
        logger.error(f"Error processing request: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)