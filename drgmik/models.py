from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=500)
    abstract = models.CharField(max_length=500)

    cover_img = ForeignKey("Image", on_delete=models.CASCADE, related_name="cover_img_fk")


class Author(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

    article = models.ManyToManyField(Article)


class Line(models.Model):
    index = models.PositiveIntegerField()
    heading = models.CharField(max_length=500, blank=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True


class Paragraph(Line):
    text = models.TextField()

    def __str__(self):
        return f"Text: {self.text}\n"


class Image(Line):
    title = models.CharField(max_length=500)
    height = models.PositiveSmallIntegerField()
    width = models.PositiveSmallIntegerField()
    img = models.ImageField(
        upload_to="uploads", height_field="height", width_field="width")

    def __str__(self):
        return f"URL: {self.img}\nTitle: {self.title}\n"
