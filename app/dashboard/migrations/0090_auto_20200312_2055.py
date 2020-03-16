# Generated by Django 2.2.4 on 2020-03-12 20:55

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0089_merge_20200310_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organizations_fk',
            field=models.ManyToManyField(blank=True, to='dashboard.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_calc_date',
            field=models.DateTimeField(default=economy.models.get_0_time),
        ),
    ]