from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Schedule(models.Model):
    DAYS = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    classroom = models.ForeignKey('core.Classroom', on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey('core.Subject', on_delete=models.SET_NULL, null=True)
    day_of_week = models.IntegerField(choices=DAYS)
    start_time = models.DateField(auto_now=True)
    end_time = models.DateField(auto_now=True)