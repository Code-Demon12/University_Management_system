from django.urls import path
from .views import SearchView

urlpatterns = [
    path("query/", SearchView.as_view(), name="query"),
]