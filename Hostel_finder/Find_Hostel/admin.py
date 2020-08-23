from django.contrib import admin

# Register your models here.
from .models import Hostels,Contact
admin.site.register(Hostels)
admin.site.register(Contact)


