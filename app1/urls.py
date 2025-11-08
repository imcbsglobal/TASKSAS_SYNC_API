from django.urls import path
from .views import (
    UploadAccUsersAPI, GetAccUsersAPI,
    UploadAccMasterAPI, GetAccMasterAPI
)

urlpatterns = [
    path('upload-users/', UploadAccUsersAPI.as_view(), name='upload_users'),
    path('get-users/', GetAccUsersAPI.as_view(), name='get_users'),
    path('upload-acc-master/', UploadAccMasterAPI.as_view(), name='upload_acc_master'),
    path('get-acc-master/', GetAccMasterAPI.as_view(), name='get_acc_master'),
]
