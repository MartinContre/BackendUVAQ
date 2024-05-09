from rest_framework import serializers

from .models import User, Post, Comment, DogBreed, DogImage, DogVote

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class DogBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogBreed
        fields = '__all__'

class DogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogImage
        fields = '__all__'

class DogVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogVote
        fields = ['image_id', 'sub_id', 'value']

