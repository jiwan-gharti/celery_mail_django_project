
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task
def add():
    for i in range(100):
        print(i)


@shared_task
def send_review_email_task(name,email,review):
    print('------------ for send mail--------------')
    context = {
        'name':name,
        'email':email,
        'review' : review
    }

    subject = "Review"
    body = render_to_string("email.txt",context)

    email = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [email,]
    )
    print("celery mail send!!!")
    return email.send(fail_silently=False)


