from django.contrib import admin

from apps.polls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
