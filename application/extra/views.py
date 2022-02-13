import xml

from django.urls import reverse_lazy, reverse
from extra_views import FormSetView, ModelFormSetView, InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from extra.forms import AddressFormSet, FlavorFormSet, TasterFormSet, TastingFormSet
from flavors.models import Flavor
from tastings.models import Taster, Tasting


class AddressFormSetView(FormSetView):
    """Define a FormSetView, a view which creates a single formset from django.forms.formset_factory and adds it to the context."""
    form_class = AddressFormSet
    template_name = 'formsets/address_formsets.html'
    success_url = reverse_lazy('flavors:list_flavor')
    factory_kwargs = {'extra': 2, 'max_num': None, 'can_order': False, 'can_delete': False}

    def formset_valid(self, formset):
        for form in formset:
            print(form.cleaned_data)
        return super(AddressFormSetView, self).formset_valid(formset)


class FlavorFormSetView(ModelFormSetView):
    """Define a ModelFormSetView, a view which works as FormSetView but instead renders a model formset using django.forms.modelformset_factory."""
    model = Flavor
    form_class = FlavorFormSet
    template_name = 'formsets/model_formset.html'
    success_url = reverse_lazy('flavors:list_flavor')
    factory_kwargs = {'extra': 2, 'max_num': None, 'can_order': False, 'can_delete': False}

    def formset_valid(self, formset):
        for form in formset:
            print(form.cleaned_data)
        return super(FlavorFormSetView, self).formset_valid(formset)

    def get_queryset(self):
        return Flavor.objects.none()


class FlavorInline(InlineFormSetFactory):
    model = Flavor
    form_class = FlavorFormSet
    factory_kwargs = {'extra': 0, 'max_num': None, 'can_order': False, 'can_delete': False}


class TasterInline(InlineFormSetFactory):
    model = Taster
    form_class = TasterFormSet
    factory_kwargs = {'extra': 0, 'max_num': None, 'can_order': False, 'can_delete': False}


class TastingInline(InlineFormSetFactory):
    model = Tasting
    form_class = TastingFormSet

    def get_factory_kwargs(self):
        kwargs = super(TastingInline, self).get_factory_kwargs()
        if self.request.path == reverse('extra:create_inline_formset'):
            kwargs['extra'] = 2
        else:
            kwargs['extra'] = 0
        kwargs['max_num'] = None
        kwargs['can_order'] = False
        kwargs['can_delete'] = False
        return kwargs


class CreateTastingView(CreateWithInlinesView):
    model = Taster
    inlines = [TastingInline]
    fields = ['name']
    template_name = 'formsets/tasting_formsets.html'
    success_url = reverse_lazy('tastings:list')


class UpdateTastingView(UpdateWithInlinesView):
    model = Taster
    inlines = [TastingInline]
    fields = ['name']
    template_name = 'formsets/tasting_formsets.html'
    success_url = reverse_lazy('tastings:list')
