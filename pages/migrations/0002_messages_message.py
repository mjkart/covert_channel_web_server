# Generated by Django 4.0.5 on 2022-07-23 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]