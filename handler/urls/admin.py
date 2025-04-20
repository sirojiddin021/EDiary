from django.urls import path, include
from rest_framework.routers import DefaultRouter
import handler.views as views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'classrooms', views.ClassroomViewSet)
router.register(r'schedule', views.ScheduleViewSet)

admin_urls = [
    path('announcements/', views.AnnouncementAPIView.as_view()),
    path('', include(router.urls)),
]
