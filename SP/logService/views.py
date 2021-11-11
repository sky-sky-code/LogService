# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework.response import Response
#
# from .models import Log, LogInstanceApp, User
# from SP.logService.api.serializers import GetAllSerializers, CreateLogSerializers
# from SP.logService.api.service import PaginationLog
#
#
# class LoggingListViewSet(viewsets.ReadOnlyModelViewSet):
#     pagination_class = PaginationLog
#
#     def get_queryset(self):
#         logging = Log.objects.all()
#         return logging
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return GetAllSerializers
#
# class LoggingCreateView(generics.CreateAPIView):
#     queryset = Log.objects.all()
#     serializer_class = CreateLogSerializers
#
# class SearchLoggingAppView(viewsets.ViewSet):
#     def list(self, request, log_app, user_email):
#         app = LogInstanceApp.objects.filter(log_instance_name=log_app).first()
#         if user_email is None:
#             queryset = Log.objects.filter(log_app=app.app_log_id)
#         else:
#             user = User.objects.filter(email=user_email)
#             queryset = Log.objects.filter(log_app=app.app_log_id, user=user.id_user)
#         serializer = GetAllSerializers(queryset, many=True)
#         return Response(serializer.data)