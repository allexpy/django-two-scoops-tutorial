from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView


from .models import User
from .forms import UserProfileForm


class TitleSearchMixin:

    def get_queryset(self):
        # Fetch the queryset from the parent's get_queryset
        queryset = super(TitleSearchMixin, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get('q')
        if q:
            # return a filtered queryset
            return queryset.filter(title__icontains=q)
        # No q is specified so we return queryset
        return queryset


class UserProfileView(LoginRequiredMixin, DetailView):
    """Gets current user's data"""
    template_name = 'user_profile.html'
    model = User

    def get_object(self, queryset=None):
        profile = get_object_or_404(User, email=self.request.user.email)
        return profile


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    """Updates current user's data"""
    template_name = 'edit_user_profile.html'
    model = User
    form_class = UserProfileForm
    success_url = '/user-profile/'

    def get_object(self, queryset=None):
        profile = get_object_or_404(User, email=self.request.user.email)
        return profile

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(EditUserProfileView, self).form_valid(form)
