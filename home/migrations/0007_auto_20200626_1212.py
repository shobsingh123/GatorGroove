# Generated by Django 2.2.8 on 2020-06-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200529_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact',
            name='tag',
            field=models.CharField(default='', max_length=122),
        ),
    ]
