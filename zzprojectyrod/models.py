from django.db import models
from .managers import DiscordUserOauth2Manager


class DiscordUser(models.Model):
    objects = DiscordUserOauth2Manager()

    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    def is_authenticated(self, request):
        return True


class LicenseKeys(models.Model):
    key = models.CharField(max_length=255)


    def __str__(self):
        return self.key