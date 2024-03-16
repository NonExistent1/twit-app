from django.urls import path

from .views import (
    TwitListView,
    TwitUpdateView,
    TwitDeleteView,
) 

urlpatterns=[
    path("<int:pk>/edit/", TwitUpdateView.as_view(), name="twit_edit"),
    path("<int:pk>/delete/", TwitDeleteView.as_view(), name="twit_delete"),
    path("", TwitListView.as_view(), name="twit_list"),
]