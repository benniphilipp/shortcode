from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import CustomUser
from django.urls import reverse

from .utils import create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

# Create your models here.
class ShortcodeClass(models.Model):
    url_destination     = models.CharField(max_length=520, unique=True, blank=False)
    url_titel           = models.CharField(max_length=125, blank=True)
    url_source          = models.CharField(max_length=525, blank=True)
    url_medium          = models.CharField(max_length=525, blank=True)
    url_campaign        = models.CharField(max_length=525, blank=True)
    url_term            = models.CharField(max_length=525, blank=True)
    url_content         = models.CharField(max_length=525, blank=True)
    url_creator         = models.ForeignKey(CustomUser,on_delete=models.CASCADE,)
    url_create_date     = models.DateTimeField(default=timezone.now)
    url_archivate       = models.BooleanField(default=False)
    url_active          = models.BooleanField(default=True)
    
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    
    def __str__(self):
        return self.url_titel
    
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url_destination:
            self.url_destination = "http://" + self.url_destination
        super(ShortcodeClass, self).save(*args, **kwargs)
    
    @property
    def archivate_count(self):
        return self.url_archivate.count()
    
    @property
    def get_short_url(self):
        url_path = self.shortcode
        return url_path