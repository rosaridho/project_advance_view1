# Generated by Django 2.1.5 on 2019-02-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20190213_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='gambar',
            field=models.ImageField(upload_to='Blog/static/img'),
        ),
    ]