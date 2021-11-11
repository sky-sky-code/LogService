from rest_framework import serializers
from ..models import LogInstanceApp, User, Log, TimeErrorApp


class TimeErrorAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = TimeErrorApp
        fields = ("__all__")

class LogInstanceAppSerializers(serializers.ModelSerializer):
    error_time = serializers.SlugRelatedField(slug_field='end_app_time', read_only=True)

    class Meta:
        model = LogInstanceApp
        fields = ("app_log_id", "log_instance_name", "start_app_time", "error_time",)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id_user", "email", "phone_number",)


class CreateLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ("__all__")

class GetAllSerializers(serializers.ModelSerializer):
    log_app = LogInstanceAppSerializers()
    user = UserSerializers()

    class Meta:
        model = Log  
        fields = ("id_log", "user_agent", "url_request", "ip_address",
                  "request_date", "response_date", "methods", "status_code",
                  "response_body", "request_body", "log_app", "user",)