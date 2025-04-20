from handler.urls.auth import auth_urls
from handler.urls.admin import admin_urls
from handler.urls.teacher import teacher_urls
from handler.urls.student import student_urls

urlpatterns = auth_urls + admin_urls + teacher_urls + student_urls