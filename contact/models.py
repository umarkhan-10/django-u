from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)  # New field
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message from {} _ {}".format(self.name, self.email)
