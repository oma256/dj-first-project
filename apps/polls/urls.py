from django.urls import path

# from apps.polls.views import polls
from apps.polls.views import PollsView

urlpatterns = [
    # path('', polls, name='index')
    path('', PollsView.as_view(), name='polls')
]