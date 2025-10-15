from django.urls import path
from .views import PostListApi, PostDetailApi

urlpatterns = [
	path("list/", PostListApi.as_view()),
	path("<int:pk>/", PostDetailApi.as_view()),
]