from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name=_('სათაური'))
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('ქვე კატეგორია'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('კატეგორია')
