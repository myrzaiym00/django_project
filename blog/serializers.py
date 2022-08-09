from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_["user"] = instance.user.username
        dict_["likes"] = instance.likes.all().count() 
        dict_["comments"] = CommentSerializers(instance.comments.all(), many=True).data
        return dict_

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        del dict_["post"]
        dict_["user"] = instance.user.username
        return dict_
