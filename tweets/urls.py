from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_tweets),
    path(
        "<int:pk>",
        views.see_one_room,
    ),
]
