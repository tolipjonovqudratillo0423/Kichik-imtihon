from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    genre = models.CharField()
    date = models.DateTimeField()
    image = models.FileField(upload_to="movie/",blank=True,null=True)
    author = models.CharField(max_length=100,blank=True,null=True)
    duration = models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.title
