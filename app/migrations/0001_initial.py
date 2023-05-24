# Generated by Django 4.2.1 on 2023-05-18 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('agent_username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TouristicSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_type', models.CharField(choices=[('NATURAL_SITE', 'Natural Site'), ('HISTORICAL_MONUMENT', 'Historical Monument'), ('RELIGIOUS_SITE', 'Religious Site'), ('LOISIRS_CENTER', 'Loisirs Center'), ('HOSTING', 'Hosting')], max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('current_stars', models.FloatField()),
                ('picture', models.ImageField(upload_to='')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='TransportMean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean_name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Wilaya',
            fields=[
                ('wilaya_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDayTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('SATURDAY', 'Saturday'), ('SUNDAY', 'Sunday'), ('MONDAY', 'Monday'), ('TUESDAY', 'Tuesday'), ('WEDNESDAY', 'Wednesday'), ('THURSDAY', 'Thursday'), ('FRIDAY', 'Friday')], max_length=255)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.touristicsite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='touristicsite',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wilaya'),
        ),
        migrations.CreateModel(
            name='SiteTransportMean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transportmean')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.touristicsite')),
            ],
        ),
        migrations.CreateModel(
            name='SiteTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.touristicsite')),
                ('work_timing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.workingdaytime')),
            ],
        ),
        migrations.CreateModel(
            name='SiteEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('created_at', models.DateField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.touristicsite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='wilaya',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wilaya'),
        ),
    ]
