from django.contrib import admin
from app2 import models
# Register your models here.
admin.site.register(models.assets)
admin.site.register(models.hosts)
admin.site.register(models.users)
admin.site.register(models.groups)