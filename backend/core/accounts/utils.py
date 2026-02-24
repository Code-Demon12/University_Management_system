from rest_framework_simplejwt.tokens import RefreshToken

def generate_tokens(user, permissions=[]):
    refresh = RefreshToken.for_user(user)

    refresh['role'] = user.role
    refresh['branch'] = user.branch.name if user.branch else None
    refresh['permissions'] = permissions

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

from django.core.mail import send_mail

def send_otp_email(email, otp):
    send_mail(
        subject="UMS Login OTP",
        message=f"Your OTP is: {otp}",
        from_email="UMS System",
        recipient_list=[email],
        fail_silently=False,
    )
