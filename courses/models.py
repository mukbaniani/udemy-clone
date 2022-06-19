from django.db import models
from django.utils.translation import gettext_lazy as _
from teacher.models import Teacher
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name=_('სათაური'))
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('ქვე კატეგორია'), blank=True, null=True)

    def __str__(self):
        return f'{self.title} -> {self.subcategory.name}'

    class Meta:
        verbose_name = _('კატეგორია')


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('სათაური'))
    about_course = models.TextField(verbose_name=_('კურსის შესახებ'))
    created_by = models.ManyToManyField(Teacher, verbose_name=_('ინსტრუქტორი'))
    language = models.CharField(max_length=90, verbose_name=_('ენა'))
    requirement = models.TextField(verbose_name=_('მოთხოვნები'))
    buyer = models.ManyToManyField(User, verbose_name=_('მყიდველი'))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _('კურსი')


class Rates(models.Model):
    RATES = [(str(i), str(i)) for i in range(1, 6)]

    rate = models.CharField(choices=RATES, verbose_name=_("შეფასება"), max_length=1)
    user = models.ManyToManyField(User, verbose_name=_("შემფასებელი"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("კურსი"))

    def __str__(self):
        return f'{self.rate}, {self.user.first_name}, {self.course.title}'

    class Meta:
        verbose_name = _("შეფასება")
