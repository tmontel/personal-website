from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    title = models.CharField(_('title'), max_length=200)
    teaser = models.TextField(_('teaser'), default='', max_length=300)
    description = models.TextField(_('description'), default='')
    date = models.DateField()
