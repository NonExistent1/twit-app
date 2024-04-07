"""
Jordyn Kuhn
CIS 218
4-7-2024
"""from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class SignUpView(CreateView):
    """Sign Up View"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class AccountUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Account Update View"""
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "account_update.html"
    success_url = reverse_lazy("twit_list") 

    def test_func(self):
        obj = self.get_object()
        return obj.pk == self.request.user.pk
