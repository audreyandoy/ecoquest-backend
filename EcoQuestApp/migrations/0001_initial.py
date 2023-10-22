# Generated by Django 4.1 on 2023-10-21 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('age', models.SmallIntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('streak', models.SmallIntegerField(blank=True, null=True)),
                ('total_points', models.SmallIntegerField(default=0)),
                ('total_co2e_reduced', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EcoTransport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=50)),
                ('distance', models.FloatField()),
                ('transport_co2_reduced', models.FloatField(blank=True, null=True)),
                ('ecoTransport_points', models.SmallIntegerField(blank=True, null=True)),
                ('activity_date', models.DateField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcoQuestApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='EcoMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eco_breakfast', models.BooleanField(default=False)),
                ('eco_lunch', models.BooleanField(default=False)),
                ('eco_dinner', models.BooleanField(default=False)),
                ('co2_reduced', models.FloatField(blank=True, null=True)),
                ('ecomeals_points', models.SmallIntegerField(blank=True, null=True)),
                ('activity_date', models.DateField(auto_now=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcoQuestApp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='EcoEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.SmallIntegerField(blank=True, null=True)),
                ('activity_date', models.DateTimeField(auto_now=True, db_index=True)),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EcoQuestApp.profile')),
            ],
        ),
    ]
