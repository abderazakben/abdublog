# Generated by Django 3.1.2 on 2020-10-26 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20201026_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Click  Link Above To Read Blog Post...', max_length=255),
        ),
    ]
