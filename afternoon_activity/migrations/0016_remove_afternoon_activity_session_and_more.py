# Generated by Django 4.2.9 on 2024-05-10 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afternoon_activity', '0015_alter_afternoon_activity_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afternoon_activity',
            name='session',
        ),
        migrations.RemoveField(
            model_name='cabin',
            name='week_one',
        ),
        migrations.RemoveField(
            model_name='session',
            name='session',
        ),
        migrations.AddField(
            model_name='session',
            name='session_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='afternoon_activity',
            name='spots_left',
            field=models.IntegerField(blank=True, default=None, help_text="Will be automatically overwritten with 'max_participants' for the activity in question.", null=True),
        ),
        migrations.CreateModel(
            name='SessionCabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afternoon_activity.cabin')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='afternoon_activity.session')),
            ],
        ),
    ]