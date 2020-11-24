from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

import sys

from ..models import User


def check_and_send_mail():
    print("user notifier starting...")
    for user in User.objects.all():
        if user.categories.count():
            categories = []
            for category in user.categories.all():
                products = []
                for product in category.products.all():
                    products.append(
                        f"<li><b>Nomi: </b>{product.name}<br/><b>Narxi: </b><i>{product.price:,} so'm</i><br/><b>Qisqacha ma'lumot: </b><i>{product.description}</i></li>"
                    )
                if not products:
                    products.append("<li>Bironta ham mahsulot topilmadi.</li>")
                categories.append(
                    f"<h3>{category.name}</h3><ul>{'<br/>'.join(products)}</ul>"
                )
            html_message = f"<p>Assalom aleykum <b>{user.full_name}</b>,\nQuyida siz kuzatayotgan bo'limlarda mavjud mahsulotlar haqida ma'lumotlar keltirilgan.</p><br/>{'<hr>'.join(categories)}<br/><br/><center>© Notifier, 2020</center>"

            try:
                send_mail(
                    subject=f"{user.full_name} uchun soatlik yangiliklar",
                    message=strip_tags(html_message),
                    html_message=html_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    auth_user=settings.EMAIL_HOST_USER,
                    auth_password=settings.EMAIL_HOST_PASSWORD
                )
            except Exception as e:
                print(f"Error while sending message to {user.full_name}: {e.args}")
            print(f"new message sent to {user.full_name}")


def start():
    print("scheduler initializing...")
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(check_and_send_mail, 'interval', hours=1, name='checking_and_sending_mails', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
