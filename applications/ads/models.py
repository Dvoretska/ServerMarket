from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Ad(TimeStampedModel):

    subject = models.CharField(_('Subject'), max_length=255)
    message = models.TextField()
    category = models.ForeignKey('Category')


class Category(models.Model):

    name = models.CharField(_('Category'), max_length=255)

    class Meta:

        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
