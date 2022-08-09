from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializers, PostSerializer
from .models import Comment, Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context["request"] = self.request
        return context

@api_view(["POST"])
def create_comment(request):
    serializer = CommentSerializers(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Вы успешно создали комментарий")

@api_view(['DELETE'])
def comment_delete(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    comment.delete()
    return Response("Ваш комментарий был успешно удален")


@api_view(['PUT', 'PATCH'])
def comment_update(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    serializer = CommentSerializers(instance=comment, data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response("Вы успешно обновили ваш комментарий")