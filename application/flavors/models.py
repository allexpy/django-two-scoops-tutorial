from django.db import models


from two_scoops.models import TimeStampedMode, User


class Flavor(TimeStampedMode):

    STATUS_0 = 0
    STATUS_1 = 1
    STATUS_2 = 2
    STATUS_3 = 3
    STATUS_4 = 4
    STATUS_5 = 5
    STATUS_CHOICES = (
        (STATUS_0, 'zero'),
        (STATUS_1, 'one'),
        (STATUS_2, 'two'),
        (STATUS_3, 'three'),
        (STATUS_4, 'four'),
        (STATUS_5, 'five'),
    )

    title = models.CharField(max_length=200)
    scoops_remaining = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_0)
    slug = models.SlugField(max_length=200, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
