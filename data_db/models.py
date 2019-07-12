from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Sample(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)    
    def __str__(self):
        return self.name


class Experiment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)    
    samples = models.ManyToManyField(Sample, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)    
    samples = models.ManyToManyField(Sample)
    published_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
