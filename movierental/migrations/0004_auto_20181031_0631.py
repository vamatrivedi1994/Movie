# Generated by Django 2.1.2 on 2018-10-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierental', '0003_auto_20181031_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rented',
            field=models.BooleanField(default=False),
        ),
    ]
