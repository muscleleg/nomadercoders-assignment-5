from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tweets.models import Tweet
from tweets.serializers import TweetSerializer


def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "all_tweets.html", {"tweets": tweets})


def see_one_room(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    return HttpResponse(tweet)


@api_view()
def tweets(request):
    all_tweets = (
        Tweet.objects.all()
    )  # QuerySet임, QuerySet을 json으로 보내려면 serialize해야함
    serializer = TweetSerializer(all_tweets, many=True)
    return Response(serializer.data)
