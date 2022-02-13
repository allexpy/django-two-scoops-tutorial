from django.db import models


from flavors.models import Flavor


class Taster(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Tasting(models.Model):
    taster = models.ForeignKey(Taster, on_delete=models.CASCADE)
    tasted_flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)

    BAD = 'bd'
    VERY_BAD = 'vb'
    GOOD = 'gd'
    VERY_GOOD = 'vg'
    OPINION_CHOICES = (
        (VERY_GOOD, 'Very Good'),
        (GOOD, 'Good'),
        (BAD, 'Bad'),
        (VERY_BAD, 'Very Bad')
    )
    opinion = models.CharField(max_length=30, choices=OPINION_CHOICES)

    def __str__(self):
        return str(self.tasted_flavor)
