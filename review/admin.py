from django.contrib import admin
from .models import Tag, report, scoring, className, teacher

admin.site.register(Tag)
admin.site.register(report)
admin.site.register(scoring)
admin.site.register(className)
admin.site.register(teacher)
