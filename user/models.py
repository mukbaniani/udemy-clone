from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext_lazy as _
from PIL import Image
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError(_('მომხმარებელს აუცილებლად უნდა ჰქონდეს მეილი'))
        elif not first_name:
            raise ValueError(_('მომხმარებელს აუცილებლად უნდა ჰქონდეს სახელი'))
        elif not last_name:
            raise ValueError(_('მომხმარებელს აუცილებლად უნდა ჰქონდეს გვარი'))
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError(_('მეილი აიცილებელია'))
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=50, verbose_name=_('სახელი'))
    last_name = models.CharField(max_length=50, verbose_name=_('გვარი'))
    email = models.EmailField(unique=True, verbose_name=_('მეილი'))
    image = models.ImageField(upload_to='images', blank=True, null=True, default='default.jpg')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('მომხმარებლები')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
