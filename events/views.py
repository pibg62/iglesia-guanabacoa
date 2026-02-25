from django.views.generic import ListView, DetailView
from .models import Event
from django.utils import timezone


class EventListView(ListView):
    model = Event
    template_name = "events/list.html"
    context_object_name = "events"

    def get_queryset(self):
        # Solo eventos futuros
        return Event.objects.filter(date__gte=timezone.now()).order_by("date")


class EventDetailView(DetailView):
    model = Event
    template_name = "events/detail.html"
