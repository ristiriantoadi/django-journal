from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Entri(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    # author=models.IntegerField()
    # username=models.CharField(max_length=100)
    # user = models.ForeignKey(User,default=User.objects.get(username="adi3d"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    # author=models.IntegerField()
    # username=models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title