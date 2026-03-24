from django.db import models
from django.contrib.auth.models import User

class UserMetaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
    
    class Meta:
        db_table = "users_metadata"
        verbose_name = "User metadata"
        verbose_name_plural = "User metadata"

# Create your models here.
