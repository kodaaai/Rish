from django.contrib import admin
from .models import Tag, report, scoring, class_info, teacher

admin.site.register(Tag)
admin.site.register(report)
admin.site.register(scoring)
admin.site.register(class_info)
admin.site.register(teacher)
