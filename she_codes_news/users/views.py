from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/createAccount.html"

@method_decorator(login_required, name='dispatch')
class AccountView(generic.DetailView):
    form_class = CustomUser
    context_object_name = 'user'
    template_name = 'users/account.html'

    def get_queryset(self):
        '''Return all user attributes.'''
        return CustomUser.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories_by_author'] = NewsStory.objects.filter(author_id = self.request.user.id).order_by("-pub_date")
        return context

