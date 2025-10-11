from django.views.generic import ListView, DetailView, TemplateView
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