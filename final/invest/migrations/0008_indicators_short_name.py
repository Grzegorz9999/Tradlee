# Generated by Django 4.0.6 on 2022-07-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0007_indicators'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicators',
            name='short_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
