from backend.accounts.tests.test_decorators import User

from .utils import (
    generate_student_credentials,
    generate_lecturer_credentials,
    send_new_account_email,
)


def post_save_account_receiver(sender, instance=None, created=False, *args, **kwargs):
    """
    Send email notification
    """
    if created:
        if instance.is_student:
            username, password = generate_student_credentials()
            instance.username = username
            instance.set_password(password)
            User.objects.filter(pk=instance.pk).update(
                username=username
            )
            instance.set_password(password)
            instance.save(update_fields=["password"])
            # Send email with the generated credentials
            send_new_account_email(instance, password)

        if instance.is_lecturer:
            username, password = generate_lecturer_credentials()
            instance.username = username
            instance.set_password(password)
            User.objects.filter(pk=instance.pk).update(
                username=username,
                password=instance.password
            )
            # Send email with the generated credentials
            send_new_account_email(instance, password)
