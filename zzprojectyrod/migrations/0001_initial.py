# Generated by Django 3.2.2 on 2021-05-09 14:24

from django.db import migrations, models
import zzprojectyrod.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('discord_tag', models.CharField(max_length=255)),
                ('avatar', models.CharField(max_length=255)),
                ('public_flags', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('locale', models.CharField(max_length=100)),
                ('mfa_enabled', models.BooleanField()),
                ('last_login', models.DateTimeField(null=True)),
            ],
            managers=[
                ('objects', zzprojectyrod.managers.DiscordUserOauth2Manager()),
            ],
        ),
    ]
