# Generated by Django 2.2.8 on 2020-01-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200112_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='Bekräftad',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='Inställd',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='Utförd',
        ),
        migrations.RemoveField(
            model_name='event',
            name='Inställd',
        ),
        migrations.AddField(
            model_name='activity',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name='Inställd'),
        ),
        migrations.AddField(
            model_name='activity',
            name='completed',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Utförd'),
        ),
        migrations.AddField(
            model_name='activity',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Bekräftad'),
        ),
        migrations.AddField(
            model_name='event',
            name='cancelled',
            field=models.BooleanField(default=False, verbose_name='Inställd'),
        ),
    ]