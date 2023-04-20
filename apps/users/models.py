from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    # username=models.CharField(max_length=40)
    # email=models.EmailField()
    phone_number=models.CharField(max_length=20, blank=False, null=False)
    created_at=models.DateField(auto_now=True, blank=False, null=False)
    age=models.PositiveIntegerField(default=18,blank=False,null=False)

    def __str__(self) -> str:
        return self.username
# Create your models here.
