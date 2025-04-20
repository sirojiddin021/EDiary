from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
import handler.permissions as permissions
import core.models as models
import transformer.serializers as sers


class UserViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdmin]
    queryset = models.User.objects.all()
    serializer_class = sers.UserSerializer


class SubjectViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminOrTeacher]
    queryset = models.Subject.objects.all()
    serializer_class = sers.SubjectSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = models.Classroom.objects.all()
    serializer_class = sers.ClassroomSerializer


class ScheduleViewSet(ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = sers.ScheduleSerializer


class AnnouncementAPIView(ListCreateAPIView):
    queryset = models.Announcement.objects.all()
    serializer_class = sers.AnnouncementSerializer