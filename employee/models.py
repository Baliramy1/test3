
from django.db import models
from django.contrib.auth.models import User


from django.dispatch import receiver
from django.urls import reverse
# from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  



class Employee(models.Model):

    Subject_Choice = (
        ('WFH', 'WFH'),
        ('Leave', 'Leave'),
        ('Casual', 'Casual'),
        ('Hafe Day', 'Hafe Day')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField( max_length=33, choices=Subject_Choice, default=False)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )