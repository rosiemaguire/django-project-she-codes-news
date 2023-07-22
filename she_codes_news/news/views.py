from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models import Q
from users.models import CustomUser
import datetime


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index') # change this to take to new story page

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.pub_date = datetime.datetime.now()
        return super().form_valid(form)

class SearchFeature(generic.ListView):
    model = NewsStory
    template_name = 'news/searchStory.html'
    context_object_name = 'searchView'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        context['author'] = CustomUser.objects.all()
        return context

    def post(self,request):
        search_query = request.POST['article_search']
        search_results =  NewsStory.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        for user in CustomUser.objects.all():
            if search_query in str(user).lower():
                search_results |= NewsStory.objects.filter(author=user.id)
            else:
                pass
        return render(request, 'news/searchStory.html', {'query': search_query,'search_results':search_results})

