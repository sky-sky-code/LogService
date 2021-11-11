# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from . import views
#
# urlpatterns = format_suffix_patterns([
#     path('log/', views.LoggingListViewSet.as_view({'get': "list"})),
#     path('log/add/', views.LoggingCreateView.as_view()),
#     path('log/<str:log_app>&<str:user_email>/', views.FilterLoggingAppView.as_view({'get': 'list'}))
#  ])