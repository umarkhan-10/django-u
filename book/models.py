from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")
    author = models.CharField(max_length=255)
    publishyear = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
