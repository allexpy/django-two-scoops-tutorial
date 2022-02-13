from django.urls import path

from . import views


app_name = 'two_scoops'

urlpatterns = [
    path('user-profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('user-profile/edit/', views.EditUserProfileView.as_view(), name='user-profile-edit'),
]
