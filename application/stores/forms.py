from django import forms


from .models import IceCreamStore


class IceCreamStoreCreateForm(forms.ModelForm):
    class Meta:
        model = IceCreamStore
        fields = ['title', 'block_address']


class IceCreamStoreUpdateForm(IceCreamStoreCreateForm):
    """Same Model, different form, making phone and description required."""

    def __init__(self, *args, **kwargs):
        super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].required = True
        self.fields['description'].required = True

    class Meta(IceCreamStoreCreateForm.Meta):
        fields = ['title', 'block_address', 'phone', 'description']
