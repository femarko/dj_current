# Generated by Django 4.2.7 on 2023-11-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_tag_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.Scope', to='articles.article'),
        ),
    ]
