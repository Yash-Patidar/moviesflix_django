# Generated by Django 3.2 on 2021-04-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210429_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Stream',
            field=models.CharField(choices=[('YouTube', 'YouTube'), ('Hotstar', 'Hotstar'), ('NF', 'Netflix'), ('PV', 'Prime Videos'), ('HU', 'hulu')], max_length=30, null=True),
        ),
    ]
