from django.urls import path
from .views import (
    UploadAccUsersAPI, GetAccUsersAPI,
    UploadMiselAPI, GetMiselAPI,
    UploadAccMasterAPI, GetAccMasterAPI,
    UploadAccLedgersAPI, GetAccLedgersAPI,
    UploadAccInvmastAPI, GetAccInvmastAPI,
    UploadCashAndBankAccMasterAPI, GetCashAndBankAccMasterAPI,
    # NEW imports
    UploadAccTtServicemasterAPI, GetAccTtServicemasterAPI,
    UploadSalesTodayAPI, GetSalesTodayAPI,
    UploadPurchaseTodayAPI, GetPurchaseTodayAPI,

    UploadSalesDaywiseAPI, GetSalesDaywiseAPI,
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

    path('upload-cashandbankaccmaster/', UploadCashAndBankAccMasterAPI.as_view(), name='upload_cashandbankaccmaster'),
    path('get-cashandbankaccmaster/', GetCashAndBankAccMasterAPI.as_view(), name='get_cashandbankaccmaster'),

    # NEW end-points
    path('upload-accttservicemaster/', UploadAccTtServicemasterAPI.as_view(), name='upload_accttservicemaster'),
    path('get-accttservicemaster/',    GetAccTtServicemasterAPI.as_view(),    name='get_accttservicemaster'),
    path('upload-sales-today/', UploadSalesTodayAPI.as_view(), name='upload_sales_today'),
    path('get-sales-today/', GetSalesTodayAPI.as_view(), name='get_sales_today'),
    path('upload-purchase-today/', UploadPurchaseTodayAPI.as_view(), name='upload_purchase_today'),
    path('get-purchase-today/', GetPurchaseTodayAPI.as_view(), name='get_purchase_today'),



    path('upload-sales-daywise/', UploadSalesDaywiseAPI.as_view(), name='upload_sales_daywise'),
    path('get-sales-daywise/', GetSalesDaywiseAPI.as_view(), name='get_sales_daywise'),


    path('upload-acc-product/', UploadAccProductAPI.as_view(), name='upload_acc_product'),
    path('get-acc-product/', GetAccProductAPI.as_view(), name='get_acc_product'),
    
    path('upload-acc-productbatch/', UploadAccProductBatchAPI.as_view(), name='upload_acc_productbatch'),
    path('get-acc-productbatch/', GetAccProductBatchAPI.as_view(), name='get_acc_productbatch'),
    
    path('upload-acc-pricecode/', UploadAccPriceCodeAPI.as_view(), name='upload_acc_pricecode'),
    path('get-acc-pricecode/', GetAccPriceCodeAPI.as_view(), name='get_acc_pricecode'),
    
    path('upload-acc-productphoto/', UploadAccProductPhotoAPI.as_view(), name='upload_acc_productphoto'),
    path('get-acc-productphoto/', GetAccProductPhotoAPI.as_view(), name='get_acc_productphoto'),
    

]
# xh