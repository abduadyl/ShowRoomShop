from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfileView.as_view()),
    path('<int:pk>/', ProfileDetailView.as_view()),
    path('update/<int:pk>/', ProfileUpdateView.as_view()),
]
