from django.urls import path

from . import views


app_name = 'sprinkles'

urlpatterns = [
    path('', views.sprinkle_list, name='list'),
    path('<int:pk>/', views.sprinkle_detail, name='details'),
    path('preview/', views.sprinkle_preview, name='preview'),
]
