from django.urls import path
from .views import *

urlpatterns = [
    path('', CurrentAffairsQuizView.as_view(), name='list'),
    path('topic/', TopicIndexView.as_view(), name='topic-index'),
    path('topic/new/', TopicCreateView.as_view(), name='topic-create'),
    path('topic/update/<slug>/', TopicUpdateView.as_view(), name='topic-update'),
    path('topic-by-file/new/', TopicFileCreateView.as_view(), name='topic-file-create'),
    path('topic/delete/<slug>/', topicDelete, name='topic-delete'),
    path('topic/<slug>/', TopicDetailView.as_view(), name='topic-detail'),
]

htmxpatterns = [
    path('topic/check/title/', checkTitle, name="topic-check-title"),
    path('topic/check/text/', checkText, name="topic-check-text"),
    path('topic-file/upload/', topicFileUpload, name="topic-file-upload"),
    path('topic/search/', topicSearch, name="topic-search"),
]

urlpatterns = htmxpatterns + urlpatterns