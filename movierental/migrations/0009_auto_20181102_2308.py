# Generated by Django 2.1.2 on 2018-11-02 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movierental', '0008_auto_20181102_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rentedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movierental.Customer'),
        ),
    ]
