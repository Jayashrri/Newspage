from django.shortcuts import render
from newspage.models import MainSite, FeedList, UserPreferences
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from . import rss

# Create your views here.

def index(request):
    return render(request, 'index.html')

class UserPreferencesDetail(DetailView):
    model=UserPreferences
    template_name='preferences_detail.html'

class UserPreferencesUpdate(UpdateView):
    model=UserPreferences
    template_name='preferences_form.html'
    fields=['display_period','articles_per_page','following_sites']

class DispTopics(DetailView):
    model=UserPreferences
    template_name='topic_list.html'

def DispFeed(request, pk):
    FeedName=FeedList.objects.get(id=pk)
    Feed=rss.GetFeed(FeedName)
    return render(request, 'feed.html', context={'Feed': Feed, 'Name': FeedName})