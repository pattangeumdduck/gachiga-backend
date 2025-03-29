from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('senior', 'Senior'),
        ('junior', 'Junior'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class SeniorUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Senior: {self.user.username}"


class JuniorUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    criminal_check_doc = models.FileField(upload_to='documents/criminal_checks/')

    def __str__(self):
        return f"Junior: {self.user.username}"
