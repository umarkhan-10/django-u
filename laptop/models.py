from django.db import models

class Laptop(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="laptops/")
    generation = models.TextField(null=True, blank=True)
    processor = models.TextField(null=True, blank=True)
    ram = models.IntegerField(null=True, blank=True)
    ssd = models.IntegerField(null=True, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True)
    detail = models.TextField(null=True, blank=True)

    def _str_(self):
        return f"Message from {self.name}"