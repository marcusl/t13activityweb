# Generated by Django 2.2.9 on 2020-01-18 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20200113_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitytype',
            options={'ordering': ['name'], 'verbose_name': 'Uppgiftstyp', 'verbose_name_plural': 'Uppgiftstyper'},
        ),
        migrations.AddField(
            model_name='member',
            name='proxy_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Member', verbose_name='Huvudman'),
        ),
    ]
