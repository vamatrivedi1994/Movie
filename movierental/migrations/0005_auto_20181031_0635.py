# Generated by Django 2.1.2 on 2018-10-31 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierental', '0004_auto_20181031_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Thriller', 'Thriller')], default='Action', max_length=15),
        ),
    ]
