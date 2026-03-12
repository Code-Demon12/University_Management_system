from django.http import JsonResponse
import json


def get_bot_response(message):

    message = message.lower()

    if "course" in message:
        return "You can find courses under Programs → Courses."

    elif "program" in message:
        return "All programs are listed in the Programs section."

    elif "quiz" in message:
        return "Quizzes are available in the Quiz section."

    elif "result" in message:
        return "Check your results in the Result section."

    elif "register" in message or "signup" in message:
        return "To create an account, click the Register button on the login page."

    elif "login" in message:
        return "Enter your username and password on the login page."

    elif "news" in message or "event" in message:
        return "Latest news and events are available on the homepage."

    elif "help" in message:
        return "You can ask me about courses, quizzes, programs, results, login or registration."

    else:
        return "Sorry, I couldn't understand. Please ask about courses, programs, quizzes or results."


def chatbot_api(request):

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        response = get_bot_response(message)

        return JsonResponse({"reply": response})