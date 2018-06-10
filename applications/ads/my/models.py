from model_utils.models import TimeStampedModel
from django.db import models


class SavedAd(TimeStampedModel):

    ad = models.ForeignKey('ads.Ad')
    user = models.ForeignKey('accounts.UserProfile')

    class Meta:
        unique_together = ('ad', 'user')
