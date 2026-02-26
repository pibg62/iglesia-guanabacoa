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


# Mixin simplificado: solo superusuarios
class SuperuserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return render(self.request, "members/no_acceso.html")


class MemberListView(SuperuserRequiredMixin, ListView):
    model = Member
    template_name = "members/member_list.html"
    context_object_name = "members"
    paginate_by = 20


class MemberDetailView(SuperuserRequiredMixin, DetailView):
    model = Member
    template_name = "members/member_detail.html"


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
