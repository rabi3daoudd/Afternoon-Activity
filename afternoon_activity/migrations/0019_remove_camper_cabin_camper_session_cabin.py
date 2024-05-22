# Generated by Django 4.2.9 on 2024-05-11 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_activity', '0018_alter_afternoon_activity_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camper',
            name='cabin',
        ),
        migrations.AddField(
            model_name='camper',
            name='session_cabin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cabin_for_camper', to='afternoon_activity.sessioncabin'),
        ),
    ]