from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to='housing_pics', blank = True)
    image2 = models.ImageField(upload_to='housing_pics', blank = True)
    image3 = models.ImageField(upload_to='housing_pics', blank = True)
    image4 = models.ImageField(upload_to='housing_pics', blank = True)
    image5 = models.ImageField(upload_to='housing_pics', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

