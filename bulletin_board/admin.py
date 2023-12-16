from django.contrib import admin
from .models import Announcement, House, Work, Other, Car


admin.site.register(Announcement)
admin.site.register(House)
admin.site.register(Work)
admin.site.register(Other)
admin.site.register(Car)
