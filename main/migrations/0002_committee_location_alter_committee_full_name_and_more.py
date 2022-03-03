# Generated by Django 4.0.1 on 2022-02-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='location',
            field=models.CharField(default='dfdsf', help_text='Enter location', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='committee',
            name='full_name',
            field=models.CharField(help_text='Enter full name', max_length=255),
        ),
        migrations.AlterField(
            model_name='committee',
            name='nickname',
            field=models.CharField(help_text='Enter nickname', max_length=255),
        ),
    ]