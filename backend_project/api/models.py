from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body

class DogBreed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DogImage(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    url = models.URLField()
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return self.id

class DogVote(models.Model):
    image_id = models.CharField(max_length=100)
    sub_id = models.CharField(max_length=100)
    value = models.IntegerField()
    
    def __str__(self):
        return f"{self.sub_id} - {self.image_id} - {self.value}"