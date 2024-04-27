# Generated by Django 5.0.4 on 2024-04-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('image', models.URLField(verbose_name='image')),
                ('release_date', models.DateField(verbose_name='release_date')),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
