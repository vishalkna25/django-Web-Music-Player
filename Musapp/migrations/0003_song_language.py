# Generated by Django 3.1.3 on 2020-11-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Musapp', '0002_auto_20201113_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='language',
            field=models.CharField(default='tamil', max_length=1000),
        ),
    ]
