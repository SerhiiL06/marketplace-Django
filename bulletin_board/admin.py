from django.contrib import admin
from .models import Announcement, House, Work, Other


admin.site.register(Announcement)
admin.site.register(House)
admin.site.register(Work)
admin.site.register(Other)
