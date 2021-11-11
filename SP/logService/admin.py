from django.contrib import admin
from .models import LogInstanceApp, Log, User, TimeErrorApp

class LogInstanceAppAdmin(admin.ModelAdmin):
    list_display = ("app_log_id", "log_instance_name", "start_app_time",)
    list_display_links = ("app_log_id",)

class LogAdmin(admin.ModelAdmin):
    list_display = ("id_log", "url_request", "request_date", "methods",
                    "status_code", )
    list_display_links = ("id_log",)

class UserAdmin(admin.ModelAdmin):
    list_display = ("id_user", "email", "phone_number",)

class TimeErrorAppAdmin(admin.ModelAdmin):
    list_display = ("id_time_error", "end_app_time", )
    list_display_links = ("id_time_error",)

admin.site.register(LogInstanceApp, LogInstanceAppAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(TimeErrorApp, TimeErrorAppAdmin)
