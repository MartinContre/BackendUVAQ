# views.py

import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView

from backend_project import settings
from api.models import Post

from .serializers import DogBreedSerializer, DogImageSerializer, DogVoteSerializer, UserSerializer, PostSerializer, CommentSerializer

DOGS_API_KEY = settings.DOGS_API_KEY

class DogBreedsList(ListAPIView):
    serializer_class = DogBreedSerializer

    def get_queryset(self):
        url = "https://api.thedogapi.com/v1/breeds"
        headers = {'x-api-key': DOGS_API_KEY}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return []

class DogImages(APIView):
    def get(self, request, breed_id):
        try:
            url = 'https://api.thecatapi.com/v1/images/search'
            headers = {'x-api-key': DOGS_API_KEY}
            params = {
                'breed_ids': breed_id,
                'include_breeds': True
            }
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            dog_images = response.json()
            print(dog_images)
            serialized_images = DogImageSerializer(data=dog_images, many=True)
            serialized_images.is_valid(raise_exception=True)
            serialized_images.save()
            return Response(serialized_images.data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            return Response({"error": f"No se pudo obtener las imágenes de perros: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": f"Error inesperado: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UsersList(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        
        return response.json()

class UserPost(APIView):
    serializer_class = PostSerializer

    def get(self, request, user_id):
        try:
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={user_id}')
            response.raise_for_status() 
            posts_data = response.json()
            
            serializer = self.serializer_class(data=posts_data, many=True)
            serializer.is_valid(raise_exception=True)
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            print(f"Error en la solicitud: {e}")
            return Response({"error": "No se pudo obtener los datos del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(f"Error inesperado: {e}")
            return Response({"error": "Ocurrió un error inesperado"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreatePost(CreateAPIView):
    serializer_class = PostSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = requests.post('https://jsonplaceholder.typicode.com/posts', json=serializer.data)
            if response.status_code == status.HTTP_201_CREATED:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = requests.post('https://jsonplaceholder.typicode.com/comments', json=serializer.data)
            if response.status_code == status.HTTP_201_CREATED:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateDogVote(CreateAPIView):
    serializer_class = DogVoteSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            url = 'https://api.thedogapi.com/v1/votes'
            headers = {'x-api-key': DOGS_API_KEY}
            response = requests.post(url, json=serializer.validated_data, headers=headers)
            if response.status_code == status.HTTP_201_CREATED:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
