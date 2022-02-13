from django.db import models


class Sprinkles(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    labels = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Sprinkle'
        verbose_name_plural = 'Sprinkles'

    def __str__(self):
        return self.name
