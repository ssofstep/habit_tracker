from rest_framework import generics
from rest_framework.permissions import AllowAny
from habits.models import Habits
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import send_telegram_message


class PublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = HabitPaginator


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)



class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit = serializer.save()
        habit.save()
        if habit.user.tg_id:
            send_telegram_message(habit.user.tg_id, "Создана новая привычка!")


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)

class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)

