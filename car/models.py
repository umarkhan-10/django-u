from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)  # allow null for migration
    image = models.ImageField(upload_to="cars/", null=True, blank=True)  # allow null
    model = models.CharField(max_length=255, null=True, blank=True)
    engine = models.TextField(max_length=255, null=True, blank=True)  # already nullable
    enginepower = models.TextField(null=True, blank=True)  # allow null
    price = models.TextField(null=True, blank=True)  # allow null
    madein = models.TextField(null=True, blank=True)  # allow null
    topspeed = models.TextField(null=True, blank=True)  # allow null

    def __str__(self):  # fix method name (two underscores)
        return f"Message from {self.name}"
