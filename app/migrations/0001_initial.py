# Generated by Django 3.2 on 2021-04-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('imdb', models.IntegerField(max_length=10)),
                ('stream', models.CharField(max_length=20)),
                ('play', models.CharField(max_length=200)),
            ],
        ),
    ]
