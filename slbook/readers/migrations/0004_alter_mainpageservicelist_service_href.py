# Generated by Django 5.1.3 on 2025-03-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0003_mainpageservicelist_service_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpageservicelist',
            name='service_href',
            field=models.CharField(blank=True, default='local', max_length=500, null=True),
        ),
    ]
