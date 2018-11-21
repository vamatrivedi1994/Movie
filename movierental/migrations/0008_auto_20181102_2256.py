# Generated by Django 2.1.2 on 2018-11-02 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movierental', '0007_remove_movie_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rentedby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movierental.Customer'),
        ),
    ]