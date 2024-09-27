from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/tweets", views.Tweets.as_view()),
]
