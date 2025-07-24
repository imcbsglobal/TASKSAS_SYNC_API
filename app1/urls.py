from django.urls import path
from .views import UploadAccUsersAPI, GetAccUsersAPI,UploadMiselAPI,GetMiselAPI

urlpatterns = [
    path('upload-users/', UploadAccUsersAPI.as_view(), name='upload_users'),
    path('get-users/', GetAccUsersAPI.as_view(), name='get_users'),


    path('upload-misel/', UploadMiselAPI.as_view(), name='upload_misel'),
    path('get-misel/', GetMiselAPI.as_view(), name='get_misel'),
]
