from django.urls import path
from .views import EventListView, EventDetailView

# Por ahora solo pon esto, luego creamos las vistas
urlpatterns = [
    path("", EventListView.as_view(), name="event_list"),
]
