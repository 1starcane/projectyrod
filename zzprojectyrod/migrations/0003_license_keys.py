# Generated by Django 3.2.2 on 2021-05-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzprojectyrod', '0002_alter_discorduser_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='License_keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255)),
            ],
        ),
    ]
