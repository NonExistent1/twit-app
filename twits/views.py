"""
Jordyn Kuhn
CIS 218
4-7-2024
"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse, reverse_lazy


from .models import Twit
from .forms import CommentForm

class TwitListView(LoginRequiredMixin, ListView):
    """Twit list view"""
    model = Twit
    template_name = "twit_list.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template"""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class TwitDetailView(LoginRequiredMixin, View):
    """Twit Detail View"""

    def get(self, request, *args, **kwargs):
        """Doing GET request"""
        view = CommentGetView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Doing POST request"""
        view = CommentPostView.as_view()
        return view(request, *args, **kwargs)

class CommentGetView(DetailView):
    """Comment Get View"""

    model = Twit
    template_name = "twit_detail.html"

    def get_context_data(self, **kwargs):
        """Get the context data for the template"""
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class CommentPostView(SingleObjectMixin, FormView):
    model = Twit
    form_class = CommentForm
    template_name = "twit_detail.html"

    def post(self, request, *args, **kwargs):
        # Get the Twit object associated with the pk in the URL
        self.object = self.get_object()
        # Do work parent would have
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """Create new comment when form is valid"""
        # Get the comment instance by saving the form, but set commit to False
        # as we don't want the form to fully save the model to the database yet
        comment = form.save(commit=False)
        # attach twit to the new comment
        comment.twit = self.object
        # attach author to new comment
        comment.author = self.request.user
        # save comment to database
        comment.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        """Get the success URL"""
        twit = self.get_object()
        return reverse("twit_detail", kwargs={"pk" : twit.pk})

class TwitCreateView(LoginRequiredMixin, CreateView):
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
    
class TwitUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Twit Update View"""

    model = Twit
    fields = (
        "body",
        "image_url",
    )
    template_name = "twit_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class TwitDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Twit Delete View"""

    model = Twit 
    template_name = "twit_delete.html"
    success_url = reverse_lazy("twit_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class TwitLikeView(LoginRequiredMixin, View):
    """Twit Like View"""

    def get(self, request, *args, **kwargs):
        """ Get Request """

        # Get out the data from the GET request
        twit_id = request.GET.get("twit_id", None)
        twit_action = request.GET.get("twit_action", None)

        if not twit_id or not twit_action:
            return JsonResponse({
                    "success": False,
                })
        
        twit = Twit.objects.get(id=twit_id)
        if twit_action == "like":
            # Do like stuff
            twit.likes.add(request.user)
        else:
            # Do unlike stuff
            twit.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True
            }
        )
    
class AccountView(LoginRequiredMixin, ListView):
    """Public Account view"""
    model = Twit
    template_name = "account_view.html"
    context_object_name = 'all_twits_by_user'

    def get_queryset(self):
        return Twit.objects.filter(author=self.kwargs['pk'])