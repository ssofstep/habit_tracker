from datetime import timedelta
from rest_framework.serializers import ValidationError


class HabitValidators:
    def __call__(self, value):
        val = dict(value)
        if val.get("complete_time") > timedelta(seconds=120):
            raise ValidationError(
                "Внимание-внимание! Время выполнения привычки не может превышать больше 2-х минут!!!!!!!!!"
            )

        elif int(val.get("periodicity")) < 1 or int(val.get("periodicity")) > 7:
            raise ValidationError(
                "Внимание-внимание! Выполняйте привычку минимум 1 раз в неделю!!!!!!!!!"
            )

        elif (
            val.get("nice_habit") is False
            and not val.get("reward")
            and not val.get("associated_habit")
        ):
            raise ValidationError(
                "Внимание-внимание! У полезной привычки необходимо заполнить одно из полей: "
                "'Вознаграждение' или 'Связанная привычка'! "
            )

        elif (
            val.get("nice_habit") is False
            and val.get("reward")
            and val.get("associated_habit")
        ):
            raise ValidationError(
                "Внимание-внимание! У полезной привычки необходимо зполнить только одно из полей:"
                " 'Вознаграждение' или 'Связанная привычка'!"
            )

        elif val.get("nice_habit") is True and val.get("associated_habit"):
            raise ValidationError(
                "Внимание-внимание! У приятной привычки не может быть связанной привычки!"
            )

        elif val.get("nice_habit") is True and val.get("reward"):
            raise ValidationError(
                "Внимание-внимание! У приятной привычки не может быть вознаграждения!"
            )
        