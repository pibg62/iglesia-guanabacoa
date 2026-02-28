from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Member
from .forms import MemberForm

from datetime import date
from django.db.models import Q


class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin que requiere superusuario, pero primero redirige al login"""

    # Esto es clave: URL a la que redirigir si no está autenticado
    login_url = "/admin/login/"  # Usa el login de Django
    redirect_field_name = "next"  # Para volver a miembros después del login

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            # Usuario autenticado pero no superusuario
            return render(self.request, "members/no_acceso.html")
        # Usuario no autenticado: redirigir al login
        return super().handle_no_permission()


class MemberListView(SuperuserRequiredMixin, ListView):
    model = Member
    template_name = "members/member_list.html"
    context_object_name = "members"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query)
                | Q(last_name1__icontains=query)
                | Q(last_name2__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_count"] = Member.objects.count()
        context["miembros_count"] = Member.objects.filter(estado="miembro").count()
        context["congregados_count"] = Member.objects.filter(
            estado="congregado"
        ).count()
        context["query"] = self.request.GET.get("q", "")
        return context


class MemberDetailView(SuperuserRequiredMixin, DetailView):
    model = Member
    template_name = "members/member_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.object
        today = date.today()
        edad = today.year - member.birth_date.year

        # Ajuste por si aún no ha cumplido años este año
        if (today.month, today.day) < (member.birth_date.month, member.birth_date.day):
            edad -= 1

        context["edad"] = edad
        return context


class MemberCreateView(SuperuserRequiredMixin, CreateView):
    model = Member
    form_class = MemberForm  # CAMBIA esto (no fields)
    template_name = "members/member_form.html"
    success_url = reverse_lazy("members:list")


class MemberUpdateView(SuperuserRequiredMixin, UpdateView):
    model = Member
    form_class = MemberForm  # CAMBIA esto (no fields)
    template_name = "members/member_form.html"
    success_url = reverse_lazy("members:list")


class MemberDeleteView(SuperuserRequiredMixin, DeleteView):
    model = Member
    template_name = "members/member_confirm_delete.html"
    success_url = reverse_lazy("members:list")
