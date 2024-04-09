from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORIES=(
    ()
)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    image = models.CharField('image url', max_length=100 )
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.id})
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.TextField(max_length=250)