from django.http import HttpResponse
from django.shortcuts import render

from tweets.models import Tweet


def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(request, "all_tweets.html", {"tweets": tweets})


def see_one_room(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    return HttpResponse(tweet)
