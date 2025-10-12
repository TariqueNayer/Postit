from django.urls import path
from .views import (Home, PostList, PostDetail, PostCreate, PostUpdate, PostDelete)

urlpatterns = [
	path('', Home.as_view(), name='home'),
	# read Views
	path('posts/', PostList.as_view(), name='post_list'),
	path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
	# full CRUD views
	path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
	path('posts/<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
	path('posts/new/', PostCreate.as_view(), name='post_create'),
]