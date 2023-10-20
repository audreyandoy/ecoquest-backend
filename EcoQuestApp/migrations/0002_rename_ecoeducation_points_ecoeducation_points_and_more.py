# Generated by Django 4.2.6 on 2023-10-20 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("EcoQuestApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ecoeducation",
            old_name="ecoEducation_points",
            new_name="points",
        ),
        migrations.RemoveField(
            model_name="ecoeducation",
            name="activity",
        ),
        migrations.AddField(
            model_name="ecoeducation",
            name="text",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="ecoeducation",
            name="activity_date",
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
