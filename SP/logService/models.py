from django.db import models
import uuid


class User(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

class TimeErrorApp(models.Model):
    id_time_error = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    end_app_time = models.DateTimeField(blank=True, null=True)


class LogInstanceApp(models.Model):
    app_log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    log_instance_name = models.CharField(max_length=255)
    start_app_time = models.DateTimeField()
    error_time = models.ForeignKey(TimeErrorApp, on_delete=models.SET_NULL, null=True, blank=True)

class Log(models.Model):
    id_log = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url_request = models.CharField(max_length=255, null=True)
    user_agent = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=15)
    request_date = models.DateTimeField()
    response_date = models.DateTimeField()
    methods = models.CharField(max_length=10, null=True)
    status_code = models.PositiveSmallIntegerField()
    request_body = models.TextField()
    response_body = models.TextField()
    log_app = models.ForeignKey(LogInstanceApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')