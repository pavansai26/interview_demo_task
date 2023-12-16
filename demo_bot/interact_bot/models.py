from django.db import models

# Create your models here.
class User(models.Model):
    """
    Model to store user data.

    Attributes:
        user_id (AutoField): Auto-incrementing primary key for each user.
        name (CharField): User's name, limited to 100 characters. Can be null or blank.
        email (EmailField): User's email address. Can be null or blank.
        phone_number (CharField): User's phone number, limited to 15 characters. Can be null or blank.
    """

    user_id = models.AutoField(primary_key=True)
    # User's name, limited to 100 characters. Can be null or blank.
    name = models.CharField(max_length=100, null=True, blank=True)
    # User's email address. Can be null or blank.
    email = models.EmailField(null=True, blank=True)
    # User's phone number, limited to 15 characters. Can be null or blank.
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    chat_history = models.TextField(blank=True)
    
    def __str__(self):
        return f"User: {self.name}"
    


class Conversation(models.Model):
    """Represents a single ongoing conversation with a user."""

    # Attribute representing the user associated with the conversation
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="conversations"
    )
    """The user associated with this conversation. Foreign key relationship to User model."""

    # Attribute representing the current topic of the conversation
    topic = models.CharField(max_length=255)
    """The current topic of the conversation. Tracks conversation flow and context."""

    # Attribute storing information collected from the user during the conversation
    data = models.JSONField(default=dict)
    """A dictionary storing information collected from the user during the conversation. Allows access and utilization of gathered data."""

    # Attribute representing the current state of the conversation flow
    state = models.CharField(max_length=255)
    """The current state of the conversation flow (e.g., greeting, data collection, confirmation). Tracks progress and transitions between stages."""

    def __str__(self):
        """Returns a string representation of the conversation."""
        # String representation of the Conversation object
        return f"Conversation: {self.topic}"


    