from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
User = get_user_model()


class Util:

    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()

    @staticmethod
    def create_random_password():
        random_password = User.objects.make_random_password(length=10,
                                                            allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789%$@&*!?')
        return random_password

    @staticmethod
    def get_encrypted_password():
        password = make_password(Util.create_random_password(), salt=None, hasher='default')
        return password
