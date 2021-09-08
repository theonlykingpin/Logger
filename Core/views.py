from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Topic


def index(request):
    return render(request, 'core/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {
        'topics': topics,
    }
    return render(request, 'core/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries
    }
    return render(request, 'core/topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:topics')
    context = {
        'form': form,
    }
    return render(request, "core/new_topic.html", context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('core:topic', topic_id=topic_id)
    context = {
        'topic': topic,
        'form': form,
    }
    return render(request, "core/new_entry.html", context)
