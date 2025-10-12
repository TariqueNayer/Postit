from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy, reverse

from .models import Post


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class PostList(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user