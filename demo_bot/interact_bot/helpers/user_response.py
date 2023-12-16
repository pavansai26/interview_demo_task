def handle_user_response(user_response, context=None):
    # Analyze user response and generate appropriate chatbot reply
    # You can use conditional statements to handle specific scenarios

    # Example: User declines sharing name
    if "name" in user_response.lower():
        return "No worries, you don't have to share your name if you're not comfortable with it. So, what brings you here today? Is there anything in particular you'd like to know or discuss?"

    # Example: User shares positive emotion
    if "great day" in user_response.lower():
        return "That's fantastic to hear! By the way, I have my birthday party coming up in a week. Could you please share your email or phone number so I can send you the invite?"