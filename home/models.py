from django.db import models

# Create your models here.

class biomasse(models.Model):
    Localité = models.CharField(max_length=40)
    Localisation = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'biomasse'

    def __str__(self):
        return self.Localité