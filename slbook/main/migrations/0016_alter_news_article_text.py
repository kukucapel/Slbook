# Generated by Django 5.1.3 on 2025-01-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_setting_count_news_on_page_alter_setting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='article_text',
            field=models.TextField(default=None, max_length=1000, null=True),
        ),
    ]
