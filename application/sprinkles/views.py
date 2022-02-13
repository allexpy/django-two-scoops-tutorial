from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


from .models import Sprinkles
from .utils import check_sprinkles
from .decorators import can_sprinkle


def sprinkle_list(request):
    """Standard list view"""
    data = dict()
    data['sprinkles'] = Sprinkles.objects.all()
    request = check_sprinkles(request)
    return render(request, 'sprinkle_list.html', data)


@can_sprinkle
def sprinkle_detail(request, pk):
    """Standard detail view"""
    data = dict()
    sprinkle = get_object_or_404(Sprinkles, pk=pk)
    data['sprinkle'] = sprinkle
    return render(request, 'sprinkle_detail.html', data)


def sprinkle_preview(request):
    """
    Preview of new sprinkle, but without the
      check_sprinkles function being used.
    """
    data = dict()
    data['sprinkles'] = Sprinkles.objects.all()
    return render(request, 'sprinkle_preview.html', data)


class SprinkleDetail(DetailView):
    """Standard detail view"""

    model = Sprinkles

    def dispatch(self, request, *args, **kwargs):
        request = check_sprinkles(request)
        return super(SprinkleDetail, self).dispatch(request, *args, **kwargs)
