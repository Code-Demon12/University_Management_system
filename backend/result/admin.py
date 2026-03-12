from django.contrib import admin
from .models import TakenCourse, Result


@admin.register(TakenCourse)
class TakenCourseAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "course",
        "total",
        "grade",
        "comment",
    )

    list_filter = (
        "course",
        "grade",
        "comment",
    )

    search_fields = (
        "student__student__username",
        "course__title",
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "semester",
        "level",
        "gpa",
        "cgpa",
    )

    list_filter = (
        "semester",
        "level",
    )