# Generated by Django 3.0.6 on 2020-05-24 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_auto_20200524_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='response_text',
        ),
    ]