from django.db import models
from django.utils import timezone


from dateutil.relativedelta import relativedelta


class VoucherManager(models.Manager):

    def age_breakdown(self):
        """Returns a dict of age brackets/counts."""
        age_brackets = []
        now = timezone.now()

        delta = now - relativedelta(years=18)
        count = self.model.objects.filter(birth_date__gt=delta).count()
        age_brackets.append(
            {'title': '0-17', 'count': count}
        )
        count = self.model.objects.filter(birth_date__lte=delta).count()
        age_brackets.append(
            {'title': '18+', 'count': count}
        )
        return age_brackets
