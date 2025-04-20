from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=2)
    students = models.ManyToManyField('core.User',limit_choices_to={'role':'student'})
    subjects = models.ManyToManyField('core.Subject')

    def __str__(self):
        return self.name