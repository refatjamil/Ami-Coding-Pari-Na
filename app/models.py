from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Khoj(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    input_values = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    