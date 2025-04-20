from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Mark(models.Model):
    student = models.ForeignKey('core.User', on_delete=models.PROTECT, related_name='mark_student', limit_choices_to={'role':'student'})
    subject = models.ForeignKey('core.Subject', on_delete=models.PROTECT, related_name='mark_teacher')
    teacher = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'teacher'})
    date = models.DateField(auto_now_add=True)
    mark = models.PositiveIntegerField(validators=(MinValueValidator(1), MaxValueValidator(5)))
    
    def __str__(self):
        return f'{self.student.username} {self.subject.name} -> {self.mark}'