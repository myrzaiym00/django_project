from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, toggle_like, create_comment, comment_update, comment_delete

router = DefaultRouter()
router.register("posts", PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/toggle_like/<int:p_id>/', toggle_like),
    path('comment_create/', create_comment),
    path('comment_update/<int:c_id>/', comment_update),
    path('comment_delete/<int:c_id>', comment_delete),
]
