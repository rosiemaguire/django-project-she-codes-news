from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        # context['stories_by_author'] = NewsStory.objects.filter(author__contains = self.request.user.id).order_by("-pub_date")
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
        return super().form_valid(form)

class SearchFeature(generic.ListView):
    form_class = StoryForm
    template_name = 'news/searchStory.html'
    context_object_name = 'searchView'
    # success_url = reverse_lazy('news:searchView')
    
    def get_queryset(self):
        '''Return all news stories.'''
        
        return NewsStory.objects.all().order_by("author")
    #

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        # context['stories_by_author'] = NewsStory.objects.filter(author_id=self.request.user.id)
                                                                # = self.request.user.id).order_by("-pub_date")
        return context

    def post(self,request):
        # Check if the request is a post request.
        # if request.method == 'POST':
            # Retrieve the search query entered by the user
            search_query = request.POST['article_search']
            # Filter your model by the search query
            stories_by_author = NewsStory.objects.filter(title__contains=search_query)
            return render(request, 'news/searchStory.html', {'query': search_query,'posts':stories_by_author})
        # else:
        #     return render(request, 'news/index.html',{})
        
