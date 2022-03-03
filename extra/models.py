from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Others(models.Model):
    '''anything can be stored in other's page'''
    title = models.CharField(
        max_length=1080, help_text="The title of your post")
    desc = RichTextField(help_text="")

    def __str__(self):
        return self.title


class Message(models.Model):
    text = RichTextField()


class Results(models.Model):
    student_name = models.CharField(max_length=1024)


class Images(models.Model):
    name = models.CharField(max_length=254)
    # image = models.ImageField(upload_to='students', default="no-images.webp")

    def __str__(self):
        return str(self.name)
