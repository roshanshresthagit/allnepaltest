from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answerreason)

