from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    user = models.ForeignKey('auth.User', null=False)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return '%d: %s visited? %s' % (self.pk, self.name, self.visited)
