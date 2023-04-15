from django.urls import path
from .views import DevicesListApiView, ProjectDetailApiView, ProjectListApiView, DevicesDetailApiView, TemplateDetailApiView, TemplateListApiView

urlpatterns = [
    path('project/', ProjectListApiView.as_view(), name="Project_List"),
    path('devices/', DevicesListApiView.as_view(), name="Devices_List"),
    path('template/', TemplateListApiView.as_view(), name="template_List"),
    path('project/<int:project_id>/', ProjectDetailApiView.as_view(), name="Project_detail"),
    path('devices/<int:device_id>/', DevicesDetailApiView.as_view(), name="Device_detail"),
    path('template/<int:template_id>/', TemplateDetailApiView.as_view(), name="Template_detail"),
]   