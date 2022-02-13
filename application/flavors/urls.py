from django.urls import path

from . import views


app_name = 'flavors'

urlpatterns = [
    path('add/', views.FlavorCreateView.as_view(), name='create_flavor'),
    path('list/', views.FlavorListView.as_view(), name='list_flavor'),
    path('list-search/', views.FlavorListView2.as_view(), name='list_flavor2'),
    path('search/', views.FlavorResultsView.as_view(), name='search'),
    path('<slug:slug>/', views.FlavorDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.FlavorUpdateView.as_view(), name='update'),
]
