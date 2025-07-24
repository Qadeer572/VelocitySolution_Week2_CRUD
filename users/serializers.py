from rest_framework import serializers

class registerSerializer(serializers.Serializer):
    email = serializers.EmailField()
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
