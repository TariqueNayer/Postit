from django.urls import path
from .views import Home, PostList, PostDetail

urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('posts/', PostList.as_view(), name='post_list'),
	path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]