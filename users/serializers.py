from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
