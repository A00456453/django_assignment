from django.db import models

# Create your models here.
from django.db import models


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200 , null= False)
    price = models.FloatField()

    def __str__(self):
        return self.name