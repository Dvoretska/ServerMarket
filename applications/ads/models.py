from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Ad(TimeStampedModel):

    subject = models.CharField(_('Subject'), max_length=255)
    message = models.TextField()
    category = models.ForeignKey('categories.Category', related_name='categories')
    location = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('accounts.UserProfile', null=True)
    price = models.IntegerField(_('Price'), default=0)
    image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Ads')

    def __str__(self):
        return self.subject
