from .models import Tweet
from .models import Like

from django.contrib import admin
from django.db.models import Func, Value, TextField


class WordFilter(admin.SimpleListFilter):
    title = "Contain or Exclude Elon Musk"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("contain", "Contain Elon Musk"),
            ("exclude", "Exclude Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()  # 선택된 값 가져오기
        target_word = "elonmusk"  # 필터링할 기준 단어 설정

        # payload에서 공백 제거 후 소문자로 변환
        cleaned_payload = Func(
            Func("payload", Value(" "), Value(""), function="REPLACE"),  # 공백 제거
            function="LOWER",  # 소문자로 변환
            output_field=TextField(),
        )

        if word == "contain":
            # 'contain'일 경우 포함되는 트윗만 필터링
            return tweets.annotate(cleaned_payload=cleaned_payload).filter(
                cleaned_payload__contains=target_word
            )
        elif word == "exclude":
            # 'exclude'일 경우 포함되지 않는 트윗만 필터링
            return tweets.annotate(cleaned_payload=cleaned_payload).exclude(
                cleaned_payload__contains=target_word
            )
        else:
            return tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "total_likes",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", WordFilter)
    search_fields = (
        "payload",
        "user__username",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at",)
    search_fields = ("user__username",)
