import random
from faker import Faker
from django.core.files.base import ContentFile
from PIL import Image
import io

from accounts.models import User, Student, Parent, DepartmentHead
from core.models import Session, Semester, NewsAndEvents
from course.models import Program, Course, Upload
from quiz.models import Quiz
from result.models import Result, TakenCourse
from payments.models import Invoice
from search.models import SearchQuery

fake = Faker()


def create_image():
    img = Image.new("RGB", (200, 200), color="blue")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), "fake.png")


def run():

    print("Generating fake dataset...")

    # Programs
    programs = []
    for _ in range(10):
        p = Program.objects.create(
            title=fake.unique.word().title(),
            summary=fake.text()
        )
        programs.append(p)

    # Users
    users = []
    for _ in range(20):
        u = User.objects.create(
            username=fake.unique.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
        )
        users.append(u)

    # Students
    students = []
    for u in users[:10]:
        s = Student.objects.create(
            student=u,
            program=random.choice(programs),
            level="Bachelor"
        )
        students.append(s)

    # Parents
    for s in students:
        Parent.objects.create(
            user=random.choice(users),
            student=s,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            relation_ship="Father"
        )

    # Sessions
    sessions = []
    for _ in range(10):
        sessions.append(
            Session.objects.create(
                session=f"{fake.year()}-{fake.year()}",
                is_current_session=False
            )
        )

    # Semester
    for s in sessions[:5]:
        Semester.objects.create(
            semester="First",
            session=s
        )

    # Courses
    courses = []
    for _ in range(10):
        c = Course.objects.create(
            title=fake.sentence(),
            code=fake.unique.word().upper(),
            credit=random.randint(1,4),
            summary=fake.text(),
            program=random.choice(programs),
            level="Bachelor",
            year=1,
            semester="First"
        )
        courses.append(c)

    # Upload files
    for c in courses:
        Upload.objects.create(
            title=fake.word(),
            course=c,
            file=create_image()
        )

    # Quiz
    quizzes = []
    for c in courses[:5]:
        quizzes.append(
            Quiz.objects.create(
                course=c,
                title=fake.word(),
                description=fake.text(),
                category="exam"
            )
        )

    # Taken courses
    for _ in range(20):
        TakenCourse.objects.create(
            student=random.choice(students),
            course=random.choice(courses),
            assignment=10,
            mid_exam=20,
            quiz=10,
            attendance=10,
            final_exam=30,
            total=80,
            grade="A",
            point=4,
            comment="PASS"
        )

    # Results
    for s in students:
        Result.objects.create(
            student=s,
            gpa=3.5,
            cgpa=3.4,
            semester="First",
            level="Bachelor"
        )

    # Invoices
    for u in users:
        Invoice.objects.create(
            user=u,
            amount=1000,
            total=1000
        )

    # Search queries
    for u in users:
        SearchQuery.objects.create(
            user=u,
            query=fake.word()
        )

    # News
    for _ in range(10):
        NewsAndEvents.objects.create(
            title=fake.sentence(),
            summary=fake.text(),
            posted_as="News",
            author=random.choice(users)
        )

    print("Fake dataset generated successfully.")