# Generated by Django 2.2.8 on 2020-01-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20200107_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='cancelled',
            new_name='Bekräftad',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='completed',
            new_name='Utförd',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='cancelled',
            new_name='Inställd',
        ),
        migrations.AddField(
            model_name='activity',
            name='Inställd',
            field=models.BooleanField(default=False),
        ),
    ]
