from django.urls import path

from . import views


app_name = 'stores'

urlpatterns = [
    path('list', views.IceCreamListView.as_view(), name='store-list'),
    path('search/', views.IceCreamSearch.as_view(), name='store-search'),
]
