from django.contrib import admin

from boards.models import Board, Topic, Post


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['board', 'subject', 'starter', 'last_updated']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['message', 'topic', 'created_by']
