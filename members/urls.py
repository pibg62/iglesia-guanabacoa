from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path("", views.MemberListView.as_view(), name="list"),
    path("nuevo/", views.MemberCreateView.as_view(), name="create"),
    path("<int:pk>/", views.MemberDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", views.MemberUpdateView.as_view(), name="update"),
    path("<int:pk>/eliminar/", views.MemberDeleteView.as_view(), name="delete"),
]
