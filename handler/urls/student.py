from django.urls import path
import handler.views as views

student_urls = [
    path('my-marks/', views.MyMarksAPIView.as_view()),
    path('my-homeworks/', views.MyHomeworksAPIView.as_view()),
    path('my-schedule/', views.MySchedule.as_view()),
]
