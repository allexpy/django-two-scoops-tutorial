from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=150)
    scoops_ordered = models.CharField(max_length=3, default=0)
    store_visits = models.CharField(max_length=3, default=0)

    def __str__(self):
        return self.name
