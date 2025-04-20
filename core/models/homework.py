from django.db import models


class Homework(models.Model):
    subject = models.ForeignKey('core.Subject', on_delete=models.PROTECT)
    teacher = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'teacher'})
    classroom = models.ForeignKey('core.Classroom', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    due_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.subject.name} {self.classroom.name}'