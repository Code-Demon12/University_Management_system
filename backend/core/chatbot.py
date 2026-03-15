import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


@csrf_exempt
def ai_chatbot(request):

    # Only accept POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    try:
        data = json.loads(request.body)
        user_message = data.get("message", "")
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    system_prompt = """
    You are an AI assistant for a University Management System.
    Help students with courses, semesters, exams and platform usage.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return JsonResponse({"reply": reply})