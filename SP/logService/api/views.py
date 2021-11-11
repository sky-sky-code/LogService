from rest_framework import viewsets, generics, views
from rest_framework.response import Response

from .serializers import GetAllSerializers, CreateLogSerializers
from ..models import Log, LogInstanceApp, User, TimeErrorApp
from .paginations import PaginationLog

class LoggingListViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = PaginationLog

    def get_queryset(self):
        logging = Log.objects.all()
        return logging

    def get_serializer_class(self):
        if self.action == 'list':
            return GetAllSerializers

class LoggingCreateView(generics.CreateAPIView):
    queryset = Log.objects.all()
    serializer_class = CreateLogSerializers

    def create(self, request, *args, **kwargs):
        # Добавление поля со временем ошибки в таблицу TimeErrorApp
        # и Связи между LogInstanceApp и TimeErrorApp
        start_status_code = str(request.data['status_code'])[0]
        print(start_status_code)
        if int(start_status_code) == 4 or int(start_status_code) == 5:
            TimeErrorApp.objects.create(end_app_time=request.data['response_date'])
            error_app = TimeErrorApp.objects.filter(end_app_time=request.data['response_date']).first()
            LogInstanceApp.objects.filter(app_log_id=request.data['log_app']).\
                update(error_time=error_app.id_time_error)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class SearchLoggingViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = PaginationLog

    def get_queryset(self):
        app = LogInstanceApp.objects.filter(log_instance_name=self.kwargs['log_app']).first()
        if 'user_email' in self.kwargs:
            user = User.objects.filter(email=self.kwargs['user_email']).first()
            logging = Log.objects.filter(log_app=app.app_log_id, user=user.id_user)
            return logging
        logging = Log.objects.filter(log_app=app.app_log_id)
        return logging

    def get_serializer_class(self):
        if self.action == 'list':
            return GetAllSerializers


class FilterLoggingView(views.APIView):

    def get(self, request, status_code, user_email):
        user = User.objects.filter(email=user_email).first()
        q = Log.objects.filter(status_code=status_code, user=user.id_user)
        serializer = GetAllSerializers(q, many=True)
        return Response(serializer.data)
