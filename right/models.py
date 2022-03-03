from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Islamic_discussion(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')


    def __str__(self):
        return self.short_name


# educational activity
class General_education(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')


    def __str__(self):
        return self.short_name


class Technical_education(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')


    def __str__(self):
        return self.short_name


class Adult_education(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')

    def __str__(self):
        return self.short_name



# page of GK

class General_knowledge(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')


    def __str__(self):
        return self.short_name


class About_student(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')

    def __str__(self):
        return self.short_name


class Book_list(models.Model):
    short_name = models.CharField( max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField( blank=True ,max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField( blank=True, help_text='Write your post here')


    def __str__(self):
        return self.short_name
