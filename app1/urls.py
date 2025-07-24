from django.urls import path
from .views import UploadAccUsersAPI, GetAccUsersAPI

urlpatterns = [
    path('upload-users/', UploadAccUsersAPI.as_view(), name='upload_users'),
    path('get-users/', GetAccUsersAPI.as_view(), name='get_users'),
]
