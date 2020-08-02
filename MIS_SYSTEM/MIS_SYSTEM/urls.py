from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('Accounts.urls')),
    path('',include('ViewProfile.urls')),
    path('',include('ViewRequest.urls')),
    path('',include('FileLeave.urls')),
    path('',include('CashAdvance.urls')),
    path('',include('MakeupClass.urls')),
    path('',include('RequestCertificate.urls')),
    path('',include('RoomTransfer.urls')),
    path('',include('ScheduleTransfer.urls')),
    path('',include('AttendanceReport.urls')),
    path('',include('MemoRouting.urls')),
    path('',include('Risograph.urls')),      
    path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
