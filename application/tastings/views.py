from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from django.views.generic import ListView, DetailView, UpdateView


from .models import Tasting


class TasteListView(ListView):
    model = Tasting
    context_object_name = 'tastings'
    template_name = 'tasting_list.html'


class TasteDetailView(DetailView):
    model = Tasting
    template_name = 'tasting_detail.html'
    context_object_name = 'tastings'

    def get_context_data(self, **kwargs):
        context = super(TasteDetailView, self).get_context_data(**kwargs)
        context['obj'] = Tasting.objects.filter(pk=self.kwargs.get('pk'))
        return context


class TasteUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasting
    template_name = 'tasting_update.html'
    fields = ['opinion']

    def get_success_url(self):
        return reverse('tastings:detail', kwargs={'pk': self.object.pk})
