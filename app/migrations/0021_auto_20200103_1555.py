# Generated by Django 2.2.8 on 2020-01-03 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200103_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email_verification_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
