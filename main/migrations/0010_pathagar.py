# Generated by Django 4.0.1 on 2022-02-15 17:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_teachers_description_teachers_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pathagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('title_of_post', models.CharField(help_text='Title of the post, max 1090 char', max_length=1090)),
                ('description', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
            options={
                'verbose_name': 'pathagar',
                'verbose_name_plural': 'pathagars',
            },
        ),
    ]
