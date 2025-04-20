from django.urls import path
import handler.views as views

teacher_urls = [
    path('marks/', views.MarkAPIView.as_view()),
    path('homeworks/', views.HomeworksAPIView.as_view()),
    path('my-subjects/', views.MySubjectsAPIView.as_view()),
]
