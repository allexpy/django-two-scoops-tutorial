import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core import  serializers

from flavors.forms import FlavorForm
from .models import Flavor
from two_scoops.views import TitleSearchMixin
from two_scoops.models import ModelFormFailuriHistory


class FlavorActionMixin:
    """Adds message to create or update views."""
    model = Flavor
    fields = ['title', 'slug', 'scoops_remaining']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

    def form_invalid(self, form):
        """Save invalid form and model data for later reference."""
        form_data = json.dumps(form.cleaned_data)
        model_data = serializers.serialize('json', [form.instance])
        model_data = model_data[1:-1]
        ModelFormFailuriHistory.objects.create(
            form_data=form_data,
            model_data=model_data
        )
        return super(FlavorActionMixin, self).form_invalid(form)


class FlavorListView(LoginRequiredMixin, ListView):
    model = Flavor
    template_name = 'flavors_list.html'

    def get_context_data(self, **kwargs):
        context = super(FlavorListView, self).get_context_data(**kwargs)
        context['flavors'] = Flavor.objects.filter(title__startswith='A')
        context['ordered_flavors'] = Flavor.objects.order_by('title')
        return context

    def get_queryset(self):
        queryset = super(FlavorListView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filtcer(title__icontains=q)
        return queryset


class FlavorResultsView(FlavorListView):
    model = Flavor
    template_name = 'search.html'


class FlavorListView2(LoginRequiredMixin, TitleSearchMixin, ListView):
    queryset = Flavor.objects.order_by('title')
    template_name = 'flavors_list2.html'
    context_object_name = 'flavors'


class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    success_url = '/flavors/list/'
    template_name = 'flavor_create.html'
    success_msg = 'Flavor created.'
    form_class = FlavorForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(FlavorCreateView, self).form_valid(form)


class FlavorDetailView(LoginRequiredMixin, DetailView):
    model = Flavor
    template_name = 'flavor_detail.html'

    def get_object(self, queryset=Flavor):
        """Get slug's object"""
        return get_object_or_404(Flavor, slug__iexact=self.kwargs['slug'])


class FlavorUpdateView(LoginRequiredMixin, FlavorActionMixin, UpdateView):
    model = Flavor
    template_name = 'flavor_edit.html'
    fields = ['title', 'slug', 'scoops_remaining']
    success_msg = 'Flavor updated!'

    def get_success_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.object.slug})
