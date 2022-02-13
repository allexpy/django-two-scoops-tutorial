from django.db import models
from django.utils import timezone


from flavors.models import Flavor


class PublishedManager(models.Manager):
    """
    Returns all queries with pub_date <= timezone.now()
    Example: FlavorReviews.objects.published()
    """
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(pub_date__lte=timezone.now())


class FlavorReview(models.Model):
    flavor = models.ForeignKey(Flavor, null=True, on_delete=models.CASCADE)
    review = models.TextField(max_length=255)
    pub_date = models.DateTimeField()

    # add our custom model manager
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return str(self.flavor)
