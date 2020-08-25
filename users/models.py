from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    display_name = models.CharField(max_length = 50, null = True, blank = True)
    homepage = models.URLField(null = True, blank = True)
    age = models.IntegerField(null = True)

    def __str__(self):
        return self.username