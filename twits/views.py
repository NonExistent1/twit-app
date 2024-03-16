from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


from .models import Twit

class TwitListView(ListView):
    """Twit list view"""
    model = Twit
    template_name = "twit_list.html"


class TwitCreateView(CreateView):
    """Twit Create View"""

    model = Twit
    fields = (
        "body",
        "image_url",
    )
    template_name = "twit_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TwitUpdateView(UpdateView):
    """Twit Update View"""

    model = Twit
    fields = (
        "body",
        "image_url",
    )
    template_name = "twit_edit.html"

class TwitDeleteView(DeleteView):
    """Twit Delete View"""

    model = Twit 
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")