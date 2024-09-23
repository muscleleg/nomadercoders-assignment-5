from django.contrib.auth.models import User
from django.db import models

from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return self.payload

    def total_likes(tweet):
        return tweet.likes.count()


class Like(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.user} likes the tweet: '{self.tweet}'"
