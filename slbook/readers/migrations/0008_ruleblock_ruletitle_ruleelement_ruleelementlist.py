# Generated by Django 5.1.3 on 2025-04-28 08:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0007_serviceelement_contact_form_href'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='RuleTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('text_title', models.CharField(blank=True, default=None, max_length=600, null=True)),
                ('optional_text_title', models.CharField(blank=True, default=None, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RuleElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('text', models.TextField(blank=True, default=None, max_length=65535, null=True)),
                ('id_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.ruleblock')),
            ],
        ),
        migrations.CreateModel(
            name='RuleElementList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_element', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('id_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readers.ruleelement')),
            ],
        ),
    ]
