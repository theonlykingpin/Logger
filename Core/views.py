from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TopicForm, EntryForm
from .models import Topic, Entry

def index(request):
    """The home page for the application"""
    return render(request, 'core/index.html')

@login_required
def topics(request):
    """Show all topics for the current user"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'core/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'core/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('core:topics')
    context = {'form': form}
    return render(request, "core/new_topic.html", context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry to a particular topic"""
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('core:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, "core/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = get_object_or_404(Entry, id=entry_id, topic__owner=request.user)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, "core/edit_entry.html", context)
