from django.views.generic import ListView, DetailView
from .models import Sermon


class SermonListView(ListView):
    model = Sermon
    template_name = "sermons/list.html"
    context_object_name = "sermons"
    paginate_by = 9


class SermonDetailView(DetailView):
    model = Sermon
    template_name = "sermons/detail.html"
