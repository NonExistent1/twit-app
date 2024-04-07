"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django.urls import path

from .views import SignUpView, AccountUpdateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/update/", AccountUpdateView.as_view(), name="account_update"),
]