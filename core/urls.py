from django.contrib import admin
from django.urls import path
from dashboard.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('time-frame/', time_frame),
    path('report-type/', report_type),
    path('frequency/', frequency),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)