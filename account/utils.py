from django.core.mail import send_mail


def send_activation_mail(user):
    activation_url = f'http://127.0.0.1:8000/api/v1/account/activate/{user.activation_code}'
    message = f"""Thank you for registering. Activate your account using the link:{activation_url}"""
    send_mail(
        'Активация аккаунта',
        message,
        'test@my_project.com',
        [user.email, ],
    )
