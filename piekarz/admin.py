from django.contrib import admin
from .models import Przepisy, Skladniki

# Register your models here.
admin.site.register(Przepisy)
admin.site.register(Skladniki)
