# from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
#decorator libraey applied to the function to change the behaveior
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, Http404

from .forms import TopicForm, EntryForm
from .models import Topic, Entry

# Create your views here.

def index(request):
    """creat view for learning_log hompages"""
    return render(request, 'learning_logs/index.html')

#Django  restrict access to certain pages to users through the @login_required decorator.
@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
  # topic = Topic.objects.get(id = topic_id)
   topic = get_object_or_404(Topic, id = topic_id)
   # Make sure the topic belongs to the current user.
   check_topic_owner(request,topic)

   entries = topic.entry_set.order_by('-date_added')
   context = {'topic': topic, 'entries': entries}
   return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """add new topice"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) #return to topic page after submit
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """"add new entry for specify topic""" 
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) #commit=false -> dont save into database
            new_entry.owner = request.user
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'topic':topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html' , context)

@login_required  
def edit_entry(request, entry_id):
    """edit entry of topic"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request,topic)

    if request.method != 'POST':
        #get prefilled entry
        form =  EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

def check_topic_owner(request,topic):
    if topic.owner != request.user:
       raise Http404