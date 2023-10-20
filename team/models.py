from django.contrib.auth import get_user_model
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(to=get_user_model(), related_name="teams")

    def __str__(self):
        return self.name
