# Generated by Django 2.1.5 on 2019-02-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20190212_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=models.TextField(max_length=1024),
        ),
    ]
