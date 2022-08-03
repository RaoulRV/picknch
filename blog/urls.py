from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('create_posts/', views.create_posts, name='create_posts'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete_post/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
]