# Generated by Django 4.2.1 on 2023-05-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_sitetransportmean_mean_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristicsite',
            name='current_stars',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='touristicsite',
            name='site_type',
            field=models.CharField(choices=[('NATURAL_SITE', 'Site naturel'), ('HISTORICAL_MONUMENT', 'Monument historique'), ('RELIGIOUS_SITE', 'Site religieux'), ('LOISIRS_CENTER', 'Centre de loisirs'), ('HOSTING', 'Hébergement')], max_length=255),
        ),
    ]
