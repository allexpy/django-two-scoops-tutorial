from django.urls import path
from . import views


app_name = 'vouchers'

urlpatterns = [
    path('name-check/', views.GreenfeldRoyView.as_view(), name='name')
]
