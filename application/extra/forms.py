from django import forms

from flavors.models import Flavor
from sprinkles.models import Sprinkles
from tastings.models import Taster, Tasting


class AddressFormSet(forms.Form):
    address = forms.CharField(max_length=200, required=True)


class AddressForm(forms.Form):
    address = forms.CharField(max_length=200, required=True)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, required=True)
    message = forms.CharField(max_length=200, required=True, widget=forms.Textarea())


class FlavorFormSet(forms.ModelForm):

    class Meta:
        model = Flavor
        fields = ['title', 'scoops_remaining', 'slug']


class TasterFormSet(forms.ModelForm):

    class Meta:
        model = Taster
        fields = ['name']


class TastingFormSet(forms.ModelForm):

    class Meta:
        model = Tasting
        fields = ['taster', 'tasted_flavor', 'opinion']
