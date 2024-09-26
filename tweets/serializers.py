from rest_framework import serializers


class TweetSerializer(serializers.Serializer):

    payload = serializers.CharField(required=True)
    user = serializers.CharField(required=True)
