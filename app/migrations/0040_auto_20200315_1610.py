# Generated by Django 2.2.10 on 2020-03-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20200302_1710'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['assigned_for_proxy'], name='app_activit_assigne_35ca12_idx'),
        ),
        migrations.AddIndex(
            model_name='activity',
            index=models.Index(fields=['earliest_bookable_date'], name='app_activit_earlies_b31b64_idx'),
        ),
        migrations.AddIndex(
            model_name='member',
            index=models.Index(fields=['user'], name='app_member_user_id_cd17d3_idx'),
        ),
    ]
