# Generated by Django 5.1.3 on 2024-11-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_news_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
