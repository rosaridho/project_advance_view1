# Generated by Django 2.1.5 on 2019-02-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_auto_20190213_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='gambar',
            field=models.ImageField(upload_to='blog'),
        ),
    ]
