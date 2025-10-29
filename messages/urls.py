from django.urls import path
from .views import MessageListView, MessageDetailView

app_name = 'messages'

urlpatterns = [
    path('', MessageListView.as_view(), name='list'),
    path('<int:pk>/', MessageDetailView.as_view(), name='detail'),
]
