# Generated by Django 4.2.4 on 2023-09-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='link',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]