# Generated by Django 4.1 on 2022-08-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=5)),
                ('features', models.ManyToManyField(to='pricing.feature')),
            ],
            options={
                'verbose_name': 'Pricing',
                'verbose_name_plural': 'Pricing',
            },
        ),
    ]
