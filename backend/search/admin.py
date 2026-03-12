from django.contrib import admin
from .models import SearchQuery


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):

    list_display = (
        "query",
        "user",
        "created_at",
    )

    search_fields = (
        "query",
    )

    list_filter = (
        "created_at",
    )