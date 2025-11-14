from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    genre = models.CharField()
    date = models.DateTimeField()
    image = models.FileField(upload_to="movie/")
    duration = models.CharField()
    def __str__(self):
        return self.title
