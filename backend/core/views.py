from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.decorators import admin_required, lecturer_required
from accounts.models import User, Student
from .forms import SessionForm, SemesterForm, NewsAndEventsForm
from .models import NewsAndEvents, ActivityLog, Session, Semester


def home(request):

    context = {
        "student_count": User.objects.filter(is_student=True).count(),
        "lecturer_count": User.objects.filter(is_lecturer=True).count(),
        "total_sessions": Session.objects.count(),
        "total_semesters": Semester.objects.count(),
        "recent_news": NewsAndEvents.objects.all().order_by("-updated_date")[:3],
    }

    return render(request, "home.html", context)

@login_required
def home_view(request):
    items = NewsAndEvents.objects.all().order_by("-updated_date")
    context = {
        "title": "News & Events",
        "items": items,
    }
    return render(request, "core/index.html", context)

@login_required
@admin_required
def dashboard_view(request):
    logs = ActivityLog.objects.select_related("user").order_by("-created_at")[:10]
    gender_count = Student.get_gender_count()

    recent_news = NewsAndEvents.objects.order_by("-updated_date")[:5]
    total_sessions = Session.objects.count()
    total_semesters = Semester.objects.count()

    context = {
        "student_count": User.objects.get_student_count(),
        "lecturer_count": User.objects.get_lecturer_count(),
        "superuser_count": User.objects.get_superuser_count(),
        "males_count": gender_count["M"],
        "females_count": gender_count["F"],
        "logs": logs,
        "recent_news": recent_news,
        "total_sessions": total_sessions,
        "total_semesters": total_semesters,
    }

    return render(request, "core/dashboard.html", context)

@login_required
@lecturer_required
def post_add(request):
    if request.method == "POST":
        form = NewsAndEventsForm(request.POST)
        title = request.POST.get("title")
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            ActivityLog.objects.create(
                user=request.user,
                action=f"Posted news: {post.title}"
            )
            messages.success(request, (title + " has been uploaded."))
            return redirect("home")
        else:
            messages.error(request, "Please correct the error(s) below.")
    else:
        form = NewsAndEventsForm()
    return render(
        request,
        "core/post_add.html",
        {
            "title": "Add Post",
            "form": form,
        },
    )


@login_required
@lecturer_required
def edit_post(request, pk):
    instance = get_object_or_404(NewsAndEvents, pk=pk)
    if request.method == "POST":
        form = NewsAndEventsForm(request.POST, instance=instance)
        title = request.POST.get("title")
        if form.is_valid():
            form.save()

            messages.success(request, (title + " has been updated."))
            return redirect("home")
        else:
            messages.error(request, "Please correct the error(s) below.")
    else:
        form = NewsAndEventsForm(instance=instance)
    return render(
        request,
        "core/post_add.html",
        {
            "title": "Edit Post",
            "form": form,
        },
    )


@login_required
@lecturer_required
def delete_post(request, pk):
    post = get_object_or_404(NewsAndEvents, pk=pk)
    title = post.title
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect("home")
    post.delete()
    ActivityLog.objects.create(
                user=request.user,
                action=f"Deleted post: {post.title}"
            )
    messages.success(request, (title + " has been deleted."))
    return redirect("home")


# ########################################################
# Session
# ########################################################
@login_required
@lecturer_required
def session_list_view(request):
    """Show list of all sessions"""
    sessions = Session.objects.all().order_by("-is_current_session", "-session")
    return render(request, "core/session_list.html", {"sessions": sessions})


@login_required
@lecturer_required
def session_add_view(request):
    """check request method, if POST we add session otherwise show empty form"""
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            is_current = form.cleaned_data.get("is_current_session")

            if is_current:
                Session.objects.filter(is_current_session=True).update(is_current_session=False)

            form.save()
            ActivityLog.objects.create(
                user=request.user,
                action="Created new session"
            )
            messages.success(request, "Session added successfully.")
            return redirect("session_list")


@login_required
@lecturer_required
def session_update_view(request, pk):
    session = Session.objects.get(pk=pk)
    if request.method == "POST":
        form = SessionForm(request.POST, instance=session)
        data = form.data.get("is_current_session")
        if data == "true":
            sessions = Session.objects.all()
            if sessions:
                for session in sessions:
                    if session.is_current_session == True:
                        unset = Session.objects.get(is_current_session=True)
                        unset.is_current_session = False
                        unset.save()

            if form.is_valid():
                form.save()
                messages.success(request, "Session updated successfully. ")
                return redirect("session_list")
        else:
            form = SessionForm(request.POST, instance=session)
            if form.is_valid():
                form.save()
                messages.success(request, "Session updated successfully. ")
                return redirect("session_list")

    else:
        form = SessionForm(instance=session)
    return render(request, "core/session_update.html", {"form": form})


@login_required
@lecturer_required
def session_delete_view(request, pk):
    session = get_object_or_404(Session, pk=pk)

    if session.is_current_session:
        messages.error(request, "You cannot delete current session")
        return redirect("session_list")
    else:
        session.delete()
        ActivityLog.objects.create(
                user=request.user,
                action="Deleted session"
            )
        messages.success(request, "Session successfully deleted")
    return redirect("session_list")


# ########################################################


# ########################################################
# Semester
# ########################################################
@login_required
@lecturer_required
def semester_list_view(request):
    semesters = Semester.objects.all().order_by("-is_current_semester", "-semester")
    return render(
        request,
        "core/semester_list.html",
        {
            "semesters": semesters,
        },
    )


@login_required
@lecturer_required
def semester_add_view(request):
    if request.method == "POST":
        form = SemesterForm(request.POST)
        if form.is_valid():
            is_current = form.cleaned_data.get("is_current_semester")
            session_instance = form.cleaned_data.get("session")

            if is_current:
                Semester.objects.filter(is_current_semester=True).update(is_current_semester=False)
                Session.objects.filter(is_current_session=True).update(is_current_session=False)

                session_instance.is_current_session = True
                session_instance.save()

            form.save()
            ActivityLog.objects.create(
                user=request.user,
                action="Created new session"
            )
            messages.success(request, "Semester added successfully.")
            return redirect("semester_list")


@login_required
@lecturer_required
def semester_update_view(request, pk):
    semester = Semester.objects.get(pk=pk)
    if request.method == "POST":
        if (
            request.POST.get("is_current_semester") == "True"
        ):  # returns string of 'True' if the user selected yes for 'is current semester'
            if form.is_valid():
                is_current = form.cleaned_data.get("is_current_semester")
                session_instance = form.cleaned_data.get("session")

                if is_current:
                    Semester.objects.filter(is_current_semester=True).update(is_current_semester=False)
                    Session.objects.filter(is_current_session=True).update(is_current_session=False)

                    session_instance.is_current_session = True
                    session_instance.save()

                form.save()
                messages.success(request, "Semester updated successfully!")
                return redirect("semester_list")
            unset_session = Session.objects.get(is_current_session=True)
            unset_session.is_current_session = False
            unset_session.save()
            new_session = request.POST.get("session")
            form = SemesterForm(request.POST, instance=semester)
            if form.is_valid():
                set_session = Session.objects.get(pk=new_session)
                set_session.is_current_session = True
                set_session.save()
                form.save()
                messages.success(request, "Semester updated successfully !")
                return redirect("semester_list")
        else:
            form = SemesterForm(request.POST, instance=semester)
            if form.is_valid():
                form.save()
                return redirect("semester_list")

    else:
        form = SemesterForm(instance=semester)
    return render(request, "core/semester_update.html", {"form": form})


@login_required
@lecturer_required
def semester_delete_view(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if semester.is_current_semester:
        messages.error(request, "You cannot delete current semester")
        return redirect("semester_list")
    else:
        semester.delete()
        ActivityLog.objects.create(
                user=request.user,
                action="Deleted semester"
            )
        messages.success(request, "Semester successfully deleted")
    return redirect("semester_list")
