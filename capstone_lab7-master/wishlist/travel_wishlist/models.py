from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    date = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
