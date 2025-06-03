from django.db import models
from django.utils.text import slugify 
# Create your models here.

class  stydent(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        return super().save(*args, **kwargs)