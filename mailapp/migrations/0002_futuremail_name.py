# Generated by Django 5.1.4 on 2025-01-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='futuremail',
            name='name',
            field=models.CharField(default='name1', max_length=20),
            preserve_default=False,
        ),
    ]
