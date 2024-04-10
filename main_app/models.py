from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS=(
    ('-', 'Not Yet Rated'),
    ('1', 'Awful'),
    ('2', 'Bad'),
    ('3', 'Decent'),
    ('4', 'Pretty Good'),
    ('5', 'Amazing')
)

RECURRING=(
    ('Y', 'Yes'),
    ('N', 'No'),
)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_index')
    
    class Meta:
        verbose_name_plural = "Categories"


class Course(models.Model):
    image = models.CharField('image url', help_text="*optional", max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(Category)
    recurring_fee = models.CharField(max_length=1, choices=RECURRING, default=RECURRING[0][0])
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])
    url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.id})
    

class Goal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=250)

    def __str__(self):
        return f"The Goal: {self.name}"

    def get_absolute_url(self):
        return reverse('goal', kwargs={'pk': self.id})