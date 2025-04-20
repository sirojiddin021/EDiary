from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey('core.User', on_delete=models.CASCADE, limit_choices_to={'role':'teacher'})

    def __str__(self):
        return self.name