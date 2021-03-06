# Generated by Django 4.0.6 on 2022-07-24 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0009_rename_indicators_indicator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=5000)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invest.indicator')),
            ],
        ),
    ]
