from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
import re
from django.core.exceptions import ValidationError

User = get_user_model()

def validate_linkedin_address(value):
    rule = '^https:\\/\\/[a-z]{2,3}\\.linkedin\\.com\\/.*$'
    if not re.search(rule, value):
        raise ValidationError("შეიყვანეთ სწორი ლინკინის მისამართი")


class Teacher(models.Model):
    profession = models.CharField(max_length=250, verbose_name=_('პროფესია'))
    linkedin_address = models.CharField(validators=[validate_linkedin_address], max_length=255)
    bio = models.TextField(verbose_name=_('ბიოგრაფია'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('ინსტრუქტორი')
