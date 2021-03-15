from django.urls import path
from .views import CartListView

urlpatterns = [
    path('<int:pk>/', CartListView.as_view()),
]
