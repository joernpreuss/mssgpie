from django.views.generic import ListView, DetailView
from .models import Message


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'
    paginate_by = 20


class MessageDetailView(DetailView):
    model = Message
    context_object_name = 'message'
