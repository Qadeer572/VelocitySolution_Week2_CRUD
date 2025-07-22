from rest_framework import serializers

class registerSerializer(serializers.Serializer):
    firstName= serializers.CharField(max_length=100, required=True)
    lastName = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    
     