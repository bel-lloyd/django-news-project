from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    ordering = ['-id']

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        print(self.request.GET.get('search'))
        search_var = self.request.GET.get('search',"")
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.filter(title__contains=(search_var))[:4]
        context['all_stories'] = NewsStory.objects.order_by("-pub_date").filter(title__contains=search_var)
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')