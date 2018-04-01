from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class Category(models.Model):

    name = models.CharField(_('Category'), max_length=255)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
