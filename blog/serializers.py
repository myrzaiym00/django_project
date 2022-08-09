from rest_framework import serializers
from .models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializers(instance.comments.all(), many=True).data
        rep["likes"] = instance.likes.all().count()
        rep["liked_by_user"] = False
        rep["user_rating"] = 0
        request = self.context.get("request")
        if request.user.is_authenticated:
            rep["liked_by_user"] = Like.objects.filter(user=request.user, product=instance).exists()
        return rep

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        del dict_["post"]
        dict_["user"] = instance.user.username
        return dict_
