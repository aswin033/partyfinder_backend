from rest_framework import serializers
from api.models import city,event

class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__' 

#serializer for events

class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'