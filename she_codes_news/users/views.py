from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"

class AccountView(generic.DetailView):
    form_class = CustomUser
    context_object_name = 'user'
    template_name = 'users/account.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return CustomUser.objects.all()
    