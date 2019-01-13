from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostUserListView, LikedPostsView

urlpatterns = [
    # Commenting out views.home to use ListView
   # path('', views.home, name = 'blog_home'),

    path('',PostListView.as_view(), name = 'blog_home'),
    path('post/userposts',PostUserListView.as_view(), name = 'post_user'),
    path('post/<int:pk>/',PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/',PostCreateView.as_view(), name = 'post_create'),
    path('about/',views.about, name = 'blog_about'),
    path('test',views.testpage, name = 'blog_test'),
    path('post/update/<int:pk>/',PostUpdateView.as_view(), name = 'post_update'),
    path('post/delete/<int:pk>/',PostDeleteView.as_view(), name = 'post_delete'),
    path('post/liked',LikedPostsView.as_view(),name = 'liked_posts')
]
