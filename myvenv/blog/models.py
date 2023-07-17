from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.TextField()  
    start_date = models.DateTimeField(default=timezone.now) 
    end_date = models.DateTimeField(blank=True, null=True)  
    is_completed = models.BooleanField(default=False)

    

    def __str__(self):
        return self.Title
    
    def mark_completed(self):
        self.is_completed = True
        self.save()