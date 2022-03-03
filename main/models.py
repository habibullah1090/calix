from django.db import models
from ckeditor.fields import RichTextField


class Adviser (models.Model):
    full_name = models.CharField(
        max_length=255, help_text='Enter full name of adviser')
    nickname = models.CharField(
        max_length=255, help_text='Enter nickname of adviser')
    position = models.CharField(
        max_length=255, blank=True, help_text='Enter position in the institute')
    short_description = RichTextField(
        blank=True, help_text='Enter description to show in the card')
    description = RichTextField(
        blank=True, help_text='Enter single page description')

    def __str__(self):
        return self.nickname


class Directors(models.Model):
    full_name = models.CharField(
        max_length=255, help_text='Enter full name')
    nickname = models.CharField(
        max_length=255, help_text='Enter nickname')
    position = models.CharField(
        max_length=255, blank=True, help_text='Enter position in the institute')

    phone = models.IntegerField(blank=True,
                                help_text="Enter phone number, i.e. +8801746671714")
    email = models.EmailField(
        blank=True, max_length=254, help_text="Enter e-mail address.")
    facebook = models.URLField(max_length=200, blank=True,
                               help_text="Enter facebook link, i.e. facebook.com/habibullah1090")

    short_description = RichTextField(
        blank=True, help_text="Short description")
    description = RichTextField(
        blank=True, help_text="Description ")

    def __str__(self):
        return self.nickname


class Committee(models.Model):
    full_name = models.CharField(
        max_length=255, help_text='Enter full name')
    nick_name = models.CharField(
        max_length=255, help_text='Enter full name')
    position = models.CharField(
        max_length=255, help_text='Enter full name')
    phone = models.IntegerField(help_text="Enter phone number")
    email = models.EmailField(
        blank=True, max_length=254, help_text="Enter e-mail address.")
    location = models.CharField(
        max_length=255, help_text='Enter location')
    description = models.TextField(
        blank=True, help_text="Some information about member")

    def __str__(self):
        return self.nick_name


class Notice(models.Model):
    title = models.CharField(max_length=254, help_text="Short title")
    title_in_body = models.CharField(
        max_length=1024, help_text="Body title title", null=True, blank=True)
    description = RichTextField(
        blank=True, help_text="Some information about the notice")

    def __str__(self):
        return self.title


class Teachers(models.Model):
    full_name = models.CharField(
        max_length=255, help_text='Enter full name')
    nick_name = models.CharField(
        blank=True, max_length=255, help_text='Enter nick name')
    position = models.CharField(max_length=255)

    phone = models.IntegerField(blank=True,
                                help_text="Enter phone number, i.e. +8801746671714")

    email = models.EmailField(
        blank=True, max_length=254, help_text="Enter e-mail address.")

    facebook = models.URLField(max_length=200, blank=True,
                               help_text="Enter facebook link, i.e. https://facebook.com/habibullah1090")

    twitter = models.URLField(max_length=200, blank=True,
                              help_text="Enter twitter link, i.e. https://twitter.com/habibullah1090")

    short_description = RichTextField(
        blank=True, help_text='Enter description to show in the card')
    description = RichTextField(
        blank=True, help_text='Enter single page description')

    def __str__(self):
        return f"{self.full_name} - {self.nick_name}"


class Students(models.Model):
    full_name = models.CharField(
        max_length=255, help_text='Enter full name')
    current_class = models.CharField(
        max_length=255, help_text='Current class')
    roll_number = models.IntegerField()
    phone = models.IntegerField(blank=True,
                                help_text="Enter phone number, i.e. +8801746671714")
    email = models.EmailField(
        blank=True, max_length=254, help_text="Enter e-mail address.")
    facebook = models.URLField(max_length=200, blank=True,
                               help_text="Enter facebook link, i.e. https://facebook.com/habibullah1090")

    def __str__(self):
        return f"{self.full_name} - {self.current_class}"


# simple
class Pathagar(models.Model):
    short_name = models.CharField(
        max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField(
        blank=True, max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField(blank=True, help_text='Write your post here')

    def __str__(self):
        return self.short_name


class Annual_report(models.Model):
    short_name = models.CharField(
        max_length=1090, help_text='Title of the post, max 1090 char')
    title_of_post = models.CharField(
        blank=True, max_length=1090, help_text='Title of the post, max 1090 char')
    description = RichTextField(blank=True, help_text='Write your post here')

    def __str__(self):
        return self.short_name


class Expectation(models.Model):
    is_display_in_webpage = models.BooleanField()

    name = models.CharField(max_length=254, help_text='Visitor"s name')
    email = models.EmailField(
        blank=True, help_text="Email address of visitor.")
    phone_number = models.IntegerField(
        blank=True, help_text="Phone number who visited")

    title_of_post = models.CharField(
        blank=True, max_length=1090, help_text='Title of the post, max 1090 char')
    what_you_say = RichTextField(blank=True, help_text='Write your post here')

    def __str__(self):
        return self.name
