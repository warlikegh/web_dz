from django.contrib import admin
from app import models

admin.site.register(models.Question)
admin.site.register(models.UserProfile)
admin.site.register(models.Tag)
