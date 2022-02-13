from django import forms
from django.forms import formset_factory

from sprinkles.models import Sprinkles
from .models import Flavor
from flavors.validators import validate_title


class FlavorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlavorForm, self).__init__(*args, **kwargs)
        self.fields['title'].validators.append(validate_title)

    class Meta:
        model = Flavor
        fields = ['title', 'slug', 'scoops_remaining']


class IceCreamOrderForm(forms.Form):
    slug = forms.ChoiceField(label='Flavor')
    toppings = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IceCreamOrderForm, self).__init__(*args, **kwargs)
        self.fields['slug'].choices = [(x.slug, x.title) for x in Flavor.objects.all()]

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Flavor.objects.get(slug=slug).scoops_remaining == 0:
            msg = 'Sorry, we are out of that flavor.'
            raise forms.ValidationError(msg)
        return slug

    def clean(self):
        cleaned_data = super(IceCreamOrderForm, self).clean()
        slug = cleaned_data.get('slug', '')
        toppings = cleaned_data.get('toppings', '')
        in_slug = 'chocolate' in slug.lower()
        in_toppings = 'chocolate' in toppings.lower()
        if in_slug and in_toppings:
            msg = 'Your order has too much chocolate.'
            raise forms.ValidationError(msg)
        return cleaned_data
