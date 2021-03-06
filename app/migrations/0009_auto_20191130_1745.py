# Generated by Django 2.2.6 on 2019-11-30 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_member_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['start_time', 'end_time', 'name'], 'verbose_name': 'Uppgift', 'verbose_name_plural': 'Uppgifter'},
        ),
        migrations.AlterModelOptions(
            name='activitytype',
            options={'verbose_name': 'Uppgiftstyp', 'verbose_name_plural': 'Uppgiftstyper'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['start_date', 'end_date', 'name'], 'verbose_name': 'Aktivitet', 'verbose_name_plural': 'Aktiviteter'},
        ),
        migrations.AlterModelOptions(
            name='eventtype',
            options={'ordering': ['name'], 'verbose_name': 'Aktivitetstyp', 'verbose_name_plural': 'Aktivitetstyper'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Medlem', 'verbose_name_plural': 'Medlemmar'},
        ),
        migrations.AlterField(
            model_name='event',
            name='files',
            field=models.ManyToManyField(blank=True, to='app.Attachment'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='files',
            field=models.ManyToManyField(blank=True, to='app.Attachment'),
        ),
    ]
