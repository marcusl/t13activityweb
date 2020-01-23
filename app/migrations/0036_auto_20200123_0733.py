# Generated by Django 2.2.6 on 2020-01-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_member_min_signup_bias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='member',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Kommentar'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email_verification_code',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Email-verifieringskod'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email_verification_code_created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Email-verifieringskod skapad'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Emailaddress verifierad'),
        ),
        migrations.AlterField(
            model_name='member',
            name='membercard_number',
            field=models.CharField(blank=True, max_length=64, verbose_name='Guldkortsnummer'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefonnnummer'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_verified',
            field=models.BooleanField(default=False, verbose_name='Telefonnummer verifierat'),
        ),
    ]
