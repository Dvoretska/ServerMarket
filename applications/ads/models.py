from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Ad(TimeStampedModel):

    slug = AutoSlugField(null=True, allow_unicode=True, default=None, unique=True, populate_from='subject')
    subject = models.CharField(_('Subject'), max_length=255)
    message = models.TextField()
    category = models.ForeignKey('categories.Category', related_name='ads')
    location = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('accounts.UserProfile', null=True)
    price = models.IntegerField(_('Price'), default=0)
    phone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = _('Ads')

    def __str__(self):
        return self.subject


class AdImageModel(models.Model):
    image = models.ImageField()
    ad = models.ForeignKey(Ad, related_name='images')
