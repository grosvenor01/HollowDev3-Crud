from django.db import models
from django.conf import settings
# Create your models here.
class power(models.Model):
    name_power = models.CharField(max_length=100)
    description_power = models.TextField()
    photo = models.FileField(upload_to=settings.MEDIA_ROOT , null=True ,  blank=True)
class gameCarecters(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=30 , choices=(('Free','Free') , ('Premium' , 'Premium')))
    photo = models.FileField(upload_to=settings.MEDIA_ROOT , null=True ,  blank=True)
    power = models.ManyToManyField(power)
