# Generated by Django 4.0.1 on 2022-02-19 12:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_annual_report_alter_pathagar_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_display_in_webpage', models.BooleanField()),
                ('name', models.CharField(help_text='Visitor"s name', max_length=254)),
                ('email', models.EmailField(blank=True, help_text='Email address of visitor.', max_length=254)),
                ('phone_number', models.IntegerField(blank=True, help_text='Phone number who visited')),
                ('title_of_post', models.CharField(blank=True, help_text='Title of the post, max 1090 char', max_length=1090)),
                ('what_you_say', ckeditor.fields.RichTextField(blank=True, help_text='Write your post here')),
            ],
        ),
        migrations.AlterField(
            model_name='committee',
            name='phone',
            field=models.IntegerField(help_text='Enter phone number'),
        ),
        migrations.AlterField(
            model_name='directors',
            name='phone',
            field=models.IntegerField(blank=True, help_text='Enter phone number, i.e. +8801746671714'),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone',
            field=models.IntegerField(blank=True, help_text='Enter phone number, i.e. +8801746671714'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='phone',
            field=models.IntegerField(blank=True, help_text='Enter phone number, i.e. +8801746671714'),
        ),
    ]
