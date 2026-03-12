from itertools import chain
from django.views.generic import ListView
from django.db.models import Q

from core.models import NewsAndEvents
from course.models import Program, Course
from quiz.models import Quiz

from .models import SearchQuery


class SearchView(ListView):

    template_name = "search/search_view.html"
    paginate_by = 20

    def get_queryset(self):

        query = self.request.GET.get("q")

        if not query:
            return []

        # Save search history
        SearchQuery.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            query=query
        )

        news = NewsAndEvents.objects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query)
        )

        programs = Program.objects.filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query)
        )

        courses = Course.objects.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query)
        )

        quizzes = Quiz.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

        results = sorted(
            chain(news, programs, courses, quizzes),
            key=lambda x: getattr(x, "created_at", None) or getattr(x, "timestamp", None),
            reverse=True
        )

        return results


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        query = self.request.GET.get("q")

        context["query"] = query
        context["count"] = len(self.object_list)

        return context