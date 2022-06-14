from django.urls import path
from .views import *

urlpatterns = [
    path('', CurrentAffairsQuizView.as_view(), name='list'),
    path('topic/new/', TopicCreateView.as_view(), name='topic-create'),
    path('topic/<title>/', TopicDetailView.as_view(), name='topic-detail'),
]
