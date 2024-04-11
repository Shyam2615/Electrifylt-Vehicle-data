from django.contrib import admin
from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('time-frame/', time_frame),
    path('report-type/', report_type),
    path('frequency/', frequency),
]
