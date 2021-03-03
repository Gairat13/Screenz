from django.core.mail import send_mail


def send_activation_mail(user):
    user.create_activation_code()
    message = f"""Thank you for registration. Please tap the link to activate your account:
    http://127.0.0.1:8000/accounts/activation/?u={user.activation_code}"""
    send_mail(
        'Аccount activation',
        message,
        'test@my_project.com',
        [user.email],
    )