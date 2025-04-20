from rest_framework import generics
from handler.permissions import IsAuthenticated, IsTeacher, IsAdminOrTeacher
import core.models as models
import transformer.serializers as sers


class MarkAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer_class = sers.MarkSerializer

    def get_queryset(self):
        return models.Mark.objects.filter(subject__teacher=self.request.user)


class HomeworksAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsTeacher]
    serializer_class = sers.HomeworkSerializer

    def get_queryset(self):
        return models.Homework.objects.filter(teacher=self.request.user)


class MySubjectsAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminOrTeacher]
    serializer_class = sers.SubjectSerializer

    def get_queryset(self):
        return models.Subject.objects.filter(teacher=self.request.user)