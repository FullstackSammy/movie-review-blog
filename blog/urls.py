from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        "delete/<int:id>",
        views.PostDetail.delete_own_comment,
        name="delete_comment",
    ),
    path(
        "edit/<int:id>",
        views.PostDetail.edit_own_comment,
        name="edit_comment",
    ),
    path(
        'contact', views.Suggestions.as_view(), name='movie_suggestions'),
]
