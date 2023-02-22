from django.db import models
from django.forms import CharField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, default='SOME STRING')
    url = models.CharField(max_length=120, default='SOME STRING', unique=True)
    picture = models.FileField()
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    submit = models.BooleanField(default=False)

    def __str__(self):
        return self.name