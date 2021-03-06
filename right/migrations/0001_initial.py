# Generated by Django 4.0.1 on 2022-02-15 18:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adult_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
        migrations.CreateModel(
            name='General_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
        migrations.CreateModel(
            name='General_knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
        migrations.CreateModel(
            name='Islamic_discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
        migrations.CreateModel(
            name='Technical_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
    ]
