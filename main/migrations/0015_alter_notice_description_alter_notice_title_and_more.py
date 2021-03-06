# Generated by Django 4.0.1 on 2022-04-18 07:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_notice_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Some information about the notice'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(help_text='Short title', max_length=254),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title_in_body',
            field=models.CharField(blank=True, help_text='Body title title', max_length=1024, null=True),
        ),
    ]
