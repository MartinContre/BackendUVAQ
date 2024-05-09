# urls.py

from django.urls import path
from .views import (
    CreateComment,
    CreatePost,
    DogBreedsList,
    DogImages,
    CreateDogVote,
    UserPost,
    UsersList,
)


urlpatterns = [
    path('dog-breeds/', DogBreedsList.as_view(), name='dog-breeds-list'),
    path('dogs/<str:breed_id>/', DogImages.as_view(), name='dog_images'),
    path('dogs/votes/', CreateDogVote.as_view(), name='create_dog_vote'),
    path('users/', UsersList.as_view(), name='users-list'),
    path('posts/<int:user_id>/', UserPost.as_view(), name='user-posts'),
    path('posts/create/', CreatePost.as_view(), name='create-post'),
    path('comments/create/', CreateComment.as_view(), name='create-comment'),
]
