from django.urls import path
from .views import *

urlpatterns = [
    path('', CurrentAffairsQuizView.as_view(), name='list')
]
