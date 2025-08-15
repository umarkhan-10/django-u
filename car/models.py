from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="cars/", null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    engine = models.TextField(max_length=255, null=True, blank=True)
    enginepower = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    madein = models.TextField(null=True, blank=True)
    topspeed = models.TextField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Car"


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255, null=True, blank=True)  # Reviewer name
    review = models.TextField(null=True, blank=True)  # Review text
    rating = models.IntegerField(default=0)  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}★ - {self.car}"
