from django.urls import path
from .views import (
    GetAccDepartmentsAPI, GetAccGoddownAPI, GetAccGoddownStockAPI, GetAccSalesTypesAPI, UploadAccDepartmentsAPI, UploadAccGoddownAPI, UploadAccGoddownStockAPI, UploadAccSalesTypesAPI, UploadAccUsersAPI, GetAccUsersAPI,
    UploadMiselAPI, GetMiselAPI,
    UploadAccMasterAPI, GetAccMasterAPI,
    UploadAccLedgersAPI, GetAccLedgersAPI,
    UploadAccInvmastAPI, GetAccInvmastAPI,
    
    # NEW imports
    UploadAccTtServicemasterAPI, GetAccTtServicemasterAPI,
    

    
    UploadAccProductAPI, GetAccProductAPI,
    UploadAccProductBatchAPI, GetAccProductBatchAPI,
    UploadAccPriceCodeAPI, GetAccPriceCodeAPI,
    UploadAccProductPhotoAPI, GetAccProductPhotoAPI,

    
)


urlpatterns = [
    path('upload-users/', UploadAccUsersAPI.as_view(), name='upload_users'),
    path('get-users/', GetAccUsersAPI.as_view(), name='get_users'),
    path('upload-misel/', UploadMiselAPI.as_view(), name='upload_misel'),
    path('get-misel/', GetMiselAPI.as_view(), name='get_misel'),

    path('upload-acc-master/', UploadAccMasterAPI.as_view(), name='upload_acc_master'),
    path('get-acc-master/', GetAccMasterAPI.as_view(), name='get_acc_master'),
    path('upload-acc-ledgers/', UploadAccLedgersAPI.as_view(), name='upload_acc_ledgers'),
    path('get-acc-ledgers/', GetAccLedgersAPI.as_view(), name='get_acc_ledgers'),
    path('upload-acc-invmast/', UploadAccInvmastAPI.as_view(), name='upload_acc_invmast'),
    path('get-acc-invmast/', GetAccInvmastAPI.as_view(), name='get_acc_invmast'),

    

    # NEW end-points
    path('upload-accttservicemaster/', UploadAccTtServicemasterAPI.as_view(), name='upload_accttservicemaster'),
    path('get-accttservicemaster/',    GetAccTtServicemasterAPI.as_view(),    name='get_accttservicemaster'),
    



    

    path('upload-acc-product/', UploadAccProductAPI.as_view(), name='upload_acc_product'),
    path('get-acc-product/', GetAccProductAPI.as_view(), name='get_acc_product'),
    
    path('upload-acc-productbatch/', UploadAccProductBatchAPI.as_view(), name='upload_acc_productbatch'),
    path('get-acc-productbatch/', GetAccProductBatchAPI.as_view(), name='get_acc_productbatch'),
    
    path('upload-acc-pricecode/', UploadAccPriceCodeAPI.as_view(), name='upload_acc_pricecode'),
    path('get-acc-pricecode/', GetAccPriceCodeAPI.as_view(), name='get_acc_pricecode'),
    
    path('upload-acc-productphoto/', UploadAccProductPhotoAPI.as_view(), name='upload_acc_productphoto'),
    path('get-acc-productphoto/', GetAccProductPhotoAPI.as_view(), name='get_acc_productphoto'),
    path('upload-acc-sales-types/', UploadAccSalesTypesAPI.as_view(), name='upload_acc_sales_types'),
    path('get-acc-sales-types/', GetAccSalesTypesAPI.as_view(), name='get_acc_sales_types'),




    path('upload-acc-goddown/', UploadAccGoddownAPI.as_view(), name='upload_acc_goddown'),
    path('get-acc-goddown/', GetAccGoddownAPI.as_view(), name='get_acc_goddown'),

    path('upload-acc-goddownstock/', UploadAccGoddownStockAPI.as_view(), name='upload_acc_goddownstock'),
    path('get-acc-goddownstock/', GetAccGoddownStockAPI.as_view(), name='get_acc_goddownstock'),

    path("upload-acc-departments/", UploadAccDepartmentsAPI.as_view()),
    path("get-acc-departments/", GetAccDepartmentsAPI.as_view()),



    

]
# xh