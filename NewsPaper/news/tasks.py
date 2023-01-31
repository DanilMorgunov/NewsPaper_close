import os

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from news.models import Category, User, Post, PostCategory
import operator
from functools import reduce
from django.template.loader import render_to_string
import datetime


@shared_task
def mailing(postCategory, text, subscribers, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Подписка на рассылку новостей категории - {postCategory}. Новая запись',
        body=text,  # это то же, что и message
        from_email=os.getenv('EMAIL_FULL'),
        to=subscribers,  # это то же, что и recipients_list
        # subscribers
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем


@shared_task
def mailing_every_monday_8am():
    cat_sub_name = list(Category.objects.values_list())
    for cat in cat_sub_name:
        subs = [list(User.objects.filter(pk=i).values_list('email', flat=True)) for i in
                list(Category.objects.filter(name=cat[1]).values_list('subscribers', flat=True))]
        subscribers = reduce(operator.concat, subs)
        category_name = cat[1]
        posts = Post.objects.filter(postCategory=cat[0]).filter(
            dateCreation__gte=datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=7)).values_list('id',
                                                                                                                'title',
                                                                                                                'text')

        if posts.exists():
            html_content = render_to_string(
                'post_created_email.html',
                {
                    'posts': posts,
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Подписка на рассылку новостей категории - {category_name}',
                from_email=os.getenv('EMAIL_FULL'),
                to=subscribers
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()