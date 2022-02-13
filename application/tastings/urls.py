from django.urls import path

from . import views


app_name = 'tastings'

urlpatterns = [
    path('', views.TasteListView.as_view(), name='list'),
    path('<int:pk>/', views.TasteDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.TasteUpdateView.as_view(), name='update'),
]
