# Generated by Django 3.2 on 2021-04-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210429_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='country',
            field=models.CharField(choices=[('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='icon',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='imdb',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='play',
            field=models.CharField(max_length=2000),
        ),
    ]
