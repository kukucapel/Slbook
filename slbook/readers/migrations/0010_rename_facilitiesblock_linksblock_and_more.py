# Generated by Django 5.1.3 on 2025-04-30 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0009_facilitiesblock_facilitieselement_facilitiestextlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FacilitiesBlock',
            new_name='LinksBlock',
        ),
        migrations.RenameModel(
            old_name='FacilitiesElement',
            new_name='LinksElement',
        ),
        migrations.RenameModel(
            old_name='FacilitiesTextList',
            new_name='LinksTextList',
        ),
    ]
