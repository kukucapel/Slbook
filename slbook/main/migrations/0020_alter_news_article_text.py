# Generated by Django 5.1.3 on 2025-01-29 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_rightmenulinks_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='article_text',
            field=models.TextField(default=None, max_length=2500, null=True),
        ),
    ]
