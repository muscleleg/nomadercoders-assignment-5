from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from users.models import User
from users.serializers import UserSerializer


class Tweets(APIView):
    def get(self, request, pk):
        try:
            target_user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        target_tweets = Tweet.objects.filter(user__id=pk)
        user_tweets = TweetSerializer(target_tweets, many=True).data
        return Response(user_tweets)
