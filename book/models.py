from django.db import models

class Authors(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="authors/")
    dateofbirth = models.DateField()
    publishedbooks = models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")
    author = models.CharField(max_length=255)
    publishyear = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
