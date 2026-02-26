from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "devocionales/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        # Solo mostrar posts publicados
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "devocionales/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        # Solo permitir ver posts publicados
        return Post.objects.filter(is_published=True)
