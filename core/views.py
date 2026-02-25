from django.views.generic import TemplateView
from sermons.models import Sermon
from events.models import Event
from datetime import datetime


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_sermons"] = Sermon.objects.order_by("-date")[:3]
        context["upcoming_events"] = Event.objects.filter(
            date__gte=datetime.now()
        ).order_by("date")[:3]
        return context


class AboutView(TemplateView):
    template_name = "about.html"
