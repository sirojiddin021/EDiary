from rest_framework import generics
import handler.permissions as permissions
import core.models as models
import transformer.serializers as sers


class MyMarksAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsStudent]
    serializer_class = sers.MarkSerializer

    def get_queryset(self):
        return models.Mark.objects.filter(student=self.request.user)


class MyHomeworksAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsStudent]
    serializer_class = sers.HomeworkSerializer

    def get_queryset(self):
        return models.Homework.objects.filter(student=self.request.user)


class MySchedule(generics.ListAPIView):
    queryset = models.Schedule.objects.all()
    serializer_class = sers.ScheduleSerializer