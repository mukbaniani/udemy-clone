from django.contrib import admin
from . import models

admin.site.register([models.Category, models.Teacher, models.Course, models.Rates, models.Section])
