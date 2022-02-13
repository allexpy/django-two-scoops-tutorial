from django.urls import path

from . import views


app_name = 'extra'

urlpatterns = [
    path('formset', views.AddressFormSetView.as_view(), name='address_formset'),
    path('model-formset', views.FlavorFormSetView.as_view(), name='model_formset'),
    path('create-formset', views.CreateTastingView.as_view(), name='create_inline_formset'),
    path('update-formset/<int:pk>', views.UpdateTastingView.as_view(), name='update_inline_formset'),
]
