from django.contrib import admin
from .models import User, ActivityPeriod


class UserAdmin(admin.ModelAdmin):
	list_display = ('u_id', 'u_name', 'u_tz')


class ActivityPeriodAdmin(admin.ModelAdmin):
	list_display = ('u_id', 'start_timestamp', 'end_timestamp')


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriod, ActivityPeriodAdmin)


