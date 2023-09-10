from django.db import models
from django.utils import timezone

from accounts.models import CustomUser
from shortcode.models import ShortcodeClass


class CustomSettings(models.Model):
    element_id = models.CharField(max_length=255, unique=True)
    settings_json = models.JSONField()


class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=255)
    icon_svg = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LinkInBio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(upload_to='link_bio_profile_images/', null=True, blank=True)
    image = models.ImageField(upload_to='link_bio_images/', null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    links = models.ManyToManyField(ShortcodeClass, blank=True)
    social_media_platforms = models.ManyToManyField('SocialMediaPlatform', blank=True)
    url_social = models.URLField(null=True, blank=True)
    custome_settings = models.ForeignKey(CustomSettings, on_delete=models.CASCADE, null=True, blank=True)
    selected_template = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class LinkInBioLink(models.Model):
    link_in_bio = models.ForeignKey(LinkInBio, on_delete=models.CASCADE)
    shortcode = models.ForeignKey(ShortcodeClass, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('link_in_bio', 'shortcode')
