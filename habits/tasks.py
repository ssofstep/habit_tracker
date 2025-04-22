from datetime import datetime, timedelta
import pytz
from celery import shared_task
from django.conf import settings
from django.utils import timezone
from habits.models import Habits
from habits.services import send_telegram_message


@shared_task()
def telegram_message():
    timezone.activate(pytz.timezone(settings.CELERY_TIMEZONE))
    zone = pytz.timezone(settings.CELERY_TIMEZONE)
    now = datetime.now(zone)
    habits = Habits.objects.all()

    for habit in habits:
        user_tg = habit.user.tg_id
        if (
            user_tg
            and now >= habit.time - timedelta(minutes=10)
            and now.date() == habit.time.date()
        ):
            if habit.is_nice:
                message = f"У тебя новое {habit.action} в {habit.time+timedelta(hours=3)} {habit.place}"
            else:
                message = f"Напоминаю: {habit.action} в {habit.time+timedelta(hours=3)} {habit.place}"

            send_telegram_message(user_tg, message)

            if habit.reward:
                send_telegram_message(user_tg, f"Поздравляю! У тебя новое: {habit.reward}")

            habit.time += timedelta(days=habit.periodicity)
            habit.save()
