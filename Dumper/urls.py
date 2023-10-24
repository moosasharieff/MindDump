from Dumper import views
from django.urls import path, re_path

app_name = "dumper"
urlpatterns = {
    path('', views.PostListView.as_view(), name='post_list_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('post/<pk>', views.PostDetailView.as_view(), name='post_detail_view'),
    path('post/new', views.CreatePostView.as_view(), name='create_post_view'),
    path('post/<pk>/edit', views.PostUpdateView.as_view(), name='edit_post_view'),
    path('post/<pk>/remove', views.PostDeleteView.as_view(), name='post_remove_view'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_view'),
    path('post/<pk>/publish', views.post_publish, name='post_publish'),
    path('post/<pk>/comment', views.add_comments_to_post, name='add_comments_to_post'),
    path('comment/<pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove', views.comment_remove, name='comment_remove')


}

