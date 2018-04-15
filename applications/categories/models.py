from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(_('Category'), max_length=255, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name
