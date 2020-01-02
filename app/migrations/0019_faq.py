# Generated by Django 2.2.8 on 2020-01-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200102_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name': 'Vanlig fråga',
                'verbose_name_plural': 'Vanliga frågor',
            },
        ),
    ]