from celery import shared_task
from django_email_verification import send_email, send_password

from users.models import CoffeeUser


@shared_task
def celery_send_email(user_id: int):
    user = CoffeeUser.objects.get(pk=user_id) 
    send_email(user) 


@shared_task
def celery_send_password(user_id: int):
    user = CoffeeUser.objects.get(pk=user_id)
    send_password(user)
