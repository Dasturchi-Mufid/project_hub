from django.contrib import admin
from . import models

admin.site.register(models.Head)
admin.site.register(models.Message)
admin.site.register(models.Portfolio)
admin.site.register(models.Resume)
admin.site.register(models.Team)
admin.site.register(models.Vacancy)