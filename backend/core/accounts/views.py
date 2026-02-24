from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, EmailOTP, RolePermission
from .utils import generate_tokens, send_otp_email
import random

@api_view(['POST'])
def login(request):
    email = request.data.get('email')

    user = User.objects.filter(email=email).first()
    if not user:
        return Response({"error":"User not found"}, status=404)

    otp = str(random.randint(100000,999999))
    EmailOTP.objects.create(user=user, otp=otp)

    send_otp_email(email, otp)

    return Response({"message":"OTP sent to email"})

@api_view(['POST'])
def verify_otp(request):
    email = request.data.get('email')
    otp = request.data.get('otp')

    user = User.objects.filter(email=email).first()
    record = EmailOTP.objects.filter(user=user, otp=otp, is_verified=False).first()

    if not record:
        return Response({"error":"Invalid OTP"}, status=400)

    record.is_verified = True
    record.save()

    # 🔐 get permissions
    perms = RolePermission.objects.filter(role__name=user.role)\
            .values_list('permission__code', flat=True)

    tokens = generate_tokens(user, list(perms))

    return Response({
        "access": tokens["access"],
        "refresh": tokens["refresh"],
        "role": user.role,
        "branch": user.branch.name if user.branch else None,
        "permissions": list(perms)
    })