from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=255, blank=True)
    credit = models.IntegerField(default=3)
    semester = models.IntegerField(null=False)

