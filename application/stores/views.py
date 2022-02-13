from django.views.generic import CreateView, UpdateView, ListView


from .models import IceCreamStore
from .forms import IceCreamStoreCreateForm, IceCreamStoreUpdateForm
from two_scoops.views import TitleSearchMixin


class IceCreamListView(TitleSearchMixin, ListView):
    model = IceCreamStore
    template_name = 'store_list.html'
    context_object_name = 'stores'


class IceCreamSearch(ListView):
    model = IceCreamStore
    template_name = 'store_search.html'


class IceCreamCreate(CreateView):
    model = IceCreamStore
    form_class = IceCreamStoreCreateForm


class IceCreamUpdate(UpdateView):
    model = IceCreamStore
    form_class = IceCreamStoreUpdateForm
