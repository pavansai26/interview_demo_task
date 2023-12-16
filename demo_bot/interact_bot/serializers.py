# yourapp/serializers.py
from rest_framework import serializers
from interact_bot.models import User, Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'