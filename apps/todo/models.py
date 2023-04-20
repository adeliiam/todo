from django.db import models
from apps.users.models import NewUser

# Create your models here.
class ToDo(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='todo/')
    user=models.ForeignKey(NewUser, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural='задания'
