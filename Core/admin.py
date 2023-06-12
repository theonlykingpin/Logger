from django.contrib import admin
from .models import Topic, Entry


@admin.register(Topic)
class TopicsAdmin(admin.modeladmin):
    pass


@admin.register(Entry)
class EntriesAdmin(admin.modeladmin):
    pass
