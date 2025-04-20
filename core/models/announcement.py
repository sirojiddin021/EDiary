from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('core.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.title