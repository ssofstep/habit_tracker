from django.db import models

from config.settings import AUTH_USER_MODEL


class Habits(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", blank=True,
                              null=True)
    place = models.CharField(max_length=200, default="Дома", verbose_name="Место")
    time = models.DateTimeField(verbose_name="Время")
    action = models.CharField(max_length=200, verbose_name="Действие")
    nice_habit = models.BooleanField(default=False, verbose_name="Признак приятной привычки", blank=True, null=True)
    associated_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Связанная привычка",
                                         blank=True, null=True)
    periodicity = models.PositiveIntegerField(verbose_name="Периодичность", blank=True, null=True)
    reward = models.CharField(max_length=200, verbose_name="Вознаграждение", blank=True, null=True)
    complete_time = models.DurationField(verbose_name="Время на выполнение", blank=True, null=True)
    is_public = models.BooleanField(default=True, verbose_name="Признак публичности", blank=True, null=True)

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
