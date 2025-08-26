from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,default=0)
    profile_picture = models.ImageField(upload_to='author_images/',default=0)
    background_image = models.ImageField(upload_to="anime_backgrounds/", null=True, blank=True,default=0)  # 🔥 yaha background
    detail = models.TextField()

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(default=0)
    image = models.ImageField(upload_to='anime_images/')
    description = models.TextField(default=0)
    release_date = models.DateField(default=0)
    genre = models.CharField(default=0)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)

    # ForeignKey se Author ko connect kiya
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="animes",
        default=1
    )

    def __str__(self):
        return self.title