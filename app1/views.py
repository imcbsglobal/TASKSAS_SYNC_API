from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccDepartments, AccGoddown, AccGoddownStock, AccSalesTypes, AccUsers, Misel, AccMaster, AccLedgers, AccInvmast, CashAndBankAccMaster, AccTtServicemaster, SalesDaywise, SalesMonthwise,SalesToday, PurchaseToday
import traceback
import logging

logger = logging.getLogger(__name__)


class UploadAccUsersAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of user items."}, status=400)

        try:
            AccUsers.objects.filter(client_id=client_id).delete()

            for item in data:
                AccUsers.objects.create(
                    id=item['id'],
                    pass_field=item['pass'],
                    role=item.get('role'),
                    accountcode=item.get('accountcode'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} users uploaded for client_id {client_id}."}, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccUsersAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccUsersAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        users = AccUsers.objects.filter(client_id=client_id)
        data = [{
            "id": u.id,
            "pass": u.pass_field,
            "role": u.role,
            "accountcode": u.accountcode,
        } for u in users]

        return Response({"count": len(data), "users": data}, status=200)


class UploadMiselAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of misel items."}, status=400)

        try:
            Misel.objects.filter(client_id=client_id).delete()

            for item in data:
                Misel.objects.create(
                    firm_name=item.get('firm_name'),
                    address=item.get('address'),
                    phones=item.get('phones'),
                    mobile=item.get('mobile'),
                    address1=item.get('address1'),
                    address2=item.get('address2'),
                    address3=item.get('address3'),
                    pagers=item.get('pagers'),
                    tinno=item.get('tinno'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} misel records uploaded for client_id {client_id}."}, status=201)

        except Exception as e:
            logger.error(f"Error in UploadMiselAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetMiselAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        misel = Misel.objects.filter(client_id=client_id)
        data = [{
            "firm_name": m.firm_name,
            "address": m.address,
            "phones": m.phones,
            "mobile": m.mobile,
            "address1": m.address1,
            "address2": m.address2,
            "address3": m.address3,
            "pagers": m.pagers,
            "tinno": m.tinno
        } for m in misel]

        return Response({"count": len(data), "misel": data}, status=200)


class UploadAccMasterAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')
        append = request.query_params.get('append', 'false').lower() == 'true'

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of acc_master items."}, status=400)

        try:
            if not append:
                AccMaster.objects.filter(client_id=client_id).delete()

            for item in data:
                AccMaster.objects.update_or_create(
                    code=item['code'],
                    client_id=client_id,
                    defaults={
                        'name': item.get('name'),
                        'super_code': item.get('super_code'),
                        'opening_balance': item.get('opening_balance'),
                        'debit': item.get('debit'),
                        'credit': item.get('credit'),

                        # NEW FIELDS
                        'address': item.get('address'),
                        'city': item.get('city'),
                        'phone': item.get('phone'),
                        'gstin': item.get('gstin'),
                        'remarkcolumntitle': item.get('remarkcolumntitle'),

                        'place': item.get('place'),
                        'phone2': item.get('phone2'),
                        'openingdepartment': item.get('openingdepartment'),
                        'area': item.get('area') if item.get('area') else None,
                    }
                )

            action = "appended" if append else "uploaded (old data cleared)"
            return Response({
                "message": f"{len(data)} acc_master records {action} for client_id {client_id}."
            }, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccMasterAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)



class GetAccMasterAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        acc_master = AccMaster.objects.filter(client_id=client_id)

        data = [{
            "code": m.code,
            "name": m.name,
            "super_code": m.super_code if m.super_code else "",
            "opening_balance": str(m.opening_balance) if m.opening_balance is not None else None,
            "debit": str(m.debit) if m.debit is not None else None,
            "credit": str(m.credit) if m.credit is not None else None,

            # NEW FIELDS
            "address": m.address,
            "city": m.city,
            "phone": m.phone,
            "gstin": m.gstin,
            "remarkcolumntitle": m.remarkcolumntitle,

            "place": m.place,
            "phone2": m.phone2,
            "openingdepartment": m.openingdepartment,
            "area": m.area if m.area else "",
        } for m in acc_master]

        return Response({"count": len(data), "acc_master": data}, status=200)


class UploadAccLedgersAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')
        append = request.query_params.get('append', 'false').lower() == 'true'

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of acc_ledgers items."}, status=400)

        try:
            if not append:
                AccLedgers.objects.filter(client_id=client_id).delete()

            for item in data:
                AccLedgers.objects.create(
                    code=item['code'],
                    particulars=item.get('particulars'),
                    debit=item.get('debit'),
                    credit=item.get('credit'),
                    entry_mode=item.get('entry_mode'),
                    entry_date=item.get('entry_date'),
                    voucher_no=item.get('voucher_no'),
                    narration=item.get('narration'),
                    super_code=item.get('super_code'),
                    client_id=client_id
                )

            action = "appended" if append else "uploaded (old data cleared)"
            return Response({"message": f"{len(data)} acc_ledgers records {action} for client_id {client_id}."}, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccLedgersAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccLedgersAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        acc_ledgers = AccLedgers.objects.filter(client_id=client_id)
        data = [{
            "code": l.code,
            "particulars": l.particulars,
            "debit": str(l.debit) if l.debit else None,
            "credit": str(l.credit) if l.credit else None,
            "entry_mode": l.entry_mode,
            "entry_date": l.entry_date.strftime('%Y-%m-%d') if l.entry_date else None,
            "voucher_no": l.voucher_no,
            "narration": l.narration,
            "super_code": l.super_code if l.super_code else ""
        } for l in acc_ledgers]

        return Response({"count": len(data), "acc_ledgers": data}, status=200)


class UploadAccInvmastAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of acc_invmast items."}, status=400)

        try:
            AccInvmast.objects.filter(client_id=client_id).delete()

            for item in data:
                AccInvmast.objects.create(
                    modeofpayment=item.get('modeofpayment'),
                    customerid=item.get('customerid'),
                    invdate=item.get('invdate'),
                    nettotal=item.get('nettotal'),
                    paid=item.get('paid'),
                    bill_ref=item.get('bill_ref'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} acc_invmast records uploaded for client_id {client_id}."}, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccInvmastAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccInvmastAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        acc_invmast = AccInvmast.objects.filter(client_id=client_id)
        data = [{
            "modeofpayment": i.modeofpayment,
            "customerid": i.customerid,
            "invdate": i.invdate.strftime('%Y-%m-%d') if i.invdate else None,
            "nettotal": str(i.nettotal) if i.nettotal else None,
            "paid": str(i.paid) if i.paid else None,
            "bill_ref": i.bill_ref
        } for i in acc_invmast]

        return Response({"count": len(data), "acc_invmast": data}, status=200)



class UploadAccTtServicemasterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            client_id = request.query_params.get('client_id')

            if not client_id:
                return Response({"error": "Missing client_id"}, status=400)

            if not isinstance(data, list):
                return Response({"error": "Expected list"}, status=400)

            # 🔥 ALWAYS CLEAR OLD DATA FIRST
            AccTtServicemaster.objects.filter(client_id=client_id).delete()

            # ✅ IF NO NEW DATA → TABLE STAYS EMPTY
            if len(data) == 0:
                return Response(
                    {"message": "Old data cleared. No new data received."},
                    status=200
                )

            created_count = 0
            for row in data:
                slno = row.get('slno')
                if slno is None:
                    continue

                AccTtServicemaster.objects.create(
                    slno=int(float(slno)),
                    type=row.get('type'),
                    code=row.get('code'),
                    name=row.get('name'),
                    client_id=client_id
                )
                created_count += 1

            return Response(
                {"message": f"{created_count} acc_tt_servicemaster rows synced"},
                status=201
            )

        except Exception as e:
            logger.error(f"UploadAccTtServicemasterAPI error: {e}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)



class GetAccTtServicemasterAPI(APIView):
    def get(self, request):
        try:
            client_id = request.query_params.get('client_id')
            if not client_id:
                return Response({"error": "Missing client_id"}, status=400)

            rows = AccTtServicemaster.objects.filter(client_id=client_id)
            data = [{
                "slno": int(r.slno),
                "type": r.type,
                "code": r.code,
                "name": r.name
            } for r in rows]
            
            return Response({"count": len(data), "acc_tt_servicemaster": data}, status=200)
            
        except Exception as e:
            logger.error(f"Error in GetAccTtServicemasterAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)

# GET http://127.0.0.1:8000/api/get-users/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-misel/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-master/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-ledgers/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-invmast/?client_id=CLIENT001


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (AccProduct, AccProductBatch, AccPriceCode, AccProductPhoto)
import traceback
import logging

logger = logging.getLogger(__name__)


# ============ ACC_PRODUCT APIs ============
class UploadAccProductAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            # 🔥 CLEAR OLD DATA ALWAYS
            AccProduct.objects.filter(client_id=client_id).delete()

            # ✅ EMPTY DB → EMPTY SERVER
            if len(data) == 0:
                return Response(
                    {"message": "Old product data cleared. No new data received."},
                    status=200
                )

            created_count = 0
            for item in data:
                if not item.get('code'):
                    continue

                AccProduct.objects.create(
                    code=item.get('code'),
                    name=item.get('name'),
                    taxcode=item.get('taxcode'),
                    product=item.get('product'),
                    brand=item.get('brand'),
                    unit=item.get('unit'),
                    defected=item.get('defected'),
                    text6=item.get('text6'),
                    settings=item.get('settings'),
                    catagory=item.get('catagory'),
                    company=item.get('company'),
                    client_id=client_id
                )
                created_count += 1

            return Response(
                {"message": f"{created_count} products synced"},
                status=201
            )

        except Exception as e:
            logger.error(f"UploadAccProductAPI error: {e}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)




class GetAccProductAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        products = AccProduct.objects.filter(client_id=client_id)

        data = [{
            "code": p.code,
            "name": p.name,
            "taxcode": p.taxcode,
            "product": p.product,
            "brand": p.brand,
            "unit": p.unit,
            "defected": p.defected,
            "text6": p.text6,
            "settings": p.settings,
            "catagory": p.catagory,
            "company": p.company,
        } for p in products]

        return Response({"count": len(data), "products": data}, status=200)




# ============ ACC_PRODUCTBATCH APIs ============
class UploadAccProductBatchAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            # 🔥 CLEAR OLD DATA
            AccProductBatch.objects.filter(client_id=client_id).delete()

            if len(data) == 0:
                return Response(
                    {"message": "Old product batch data cleared. No new data received."},
                    status=200
                )

            created_count = 0
            for item in data:
                if not item.get('productcode'):
                    continue

                AccProductBatch.objects.create(
                    productcode=item.get('productcode'),
                    salesprice=item.get('salesprice'),
                    secondprice=item.get('secondprice'),
                    thirdprice=item.get('thirdprice'),
                    fourthprice=item.get('fourthprice'),
                    nlc1=item.get('nlc1'),
                    quantity=item.get('quantity'),
                    barcode=item.get('barcode'),
                    bmrp=item.get('bmrp'),
                    cost=item.get('cost'),
                    expirydate=item.get('expirydate'),
                    modified=item.get('modified'),
                    modifiedtime=item.get('modifiedtime'),
                    settings=item.get('settings'),
                    client_id=client_id
                )
                created_count += 1

            return Response(
                {"message": f"{created_count} product batches synced"},
                status=201
            )

        except Exception as e:
            return Response({"error": str(e)}, status=500)



class GetAccProductBatchAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        batches = AccProductBatch.objects.filter(client_id=client_id)
        data = [{
            "productcode": b.productcode,
            "salesprice": str(b.salesprice) if b.salesprice else None,
            "secondprice": str(b.secondprice) if b.secondprice else None,
            "thirdprice": str(b.thirdprice) if b.thirdprice else None,
            "fourthprice": str(b.fourthprice) if b.fourthprice else None,
            "nlc1": str(b.nlc1) if b.nlc1 else None,
            "quantity": str(b.quantity) if b.quantity else None,
            "barcode": b.barcode,
            "bmrp": str(b.bmrp) if b.bmrp else None,
            "cost": str(b.cost) if b.cost else None,
            "expirydate": b.expirydate.strftime('%Y-%m-%d') if b.expirydate else None,
            "modified": b.modified.strftime('%Y-%m-%d') if b.modified else None,
            "modifiedtime": b.modifiedtime.strftime('%H:%M:%S') if b.modifiedtime else None,
            "settings": b.settings,
        } for b in batches]

        return Response({"count": len(data), "product_batches": data}, status=200)


# ============ ACC_PRICECODE APIs ============
class UploadAccPriceCodeAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of price code items."}, status=400)

        try:
            AccPriceCode.objects.filter(client_id=client_id).delete()

            created_count = 0
            for item in data:
                if not item.get('code'):
                    continue
                
                AccPriceCode.objects.create(
                    code=item['code'],
                    name=item.get('name', ''),
                    client_id=client_id
                )
                created_count += 1

            return Response({
                "message": f"{created_count} price codes uploaded for client_id {client_id}."
            }, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccPriceCodeAPI: {str(e)}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccPriceCodeAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        price_codes = AccPriceCode.objects.filter(client_id=client_id)
        data = [{
            "code": pc.code,
            "name": pc.name,
        } for pc in price_codes]

        return Response({"count": len(data), "price_codes": data}, status=200)


# ============ ACC_PRODUCTPHOTO APIs ============
class UploadAccProductPhotoAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            # 🔥 CLEAR OLD DATA
            AccProductPhoto.objects.filter(client_id=client_id).delete()

            if len(data) == 0:
                return Response(
                    {"message": "Old product photos cleared. No new data received."},
                    status=200
                )

            created_count = 0
            for item in data:
                AccProductPhoto.objects.create(
                    code=item.get('code'),
                    url=item.get('url'),
                    client_id=client_id
                )
                created_count += 1

            return Response(
                {"message": f"{created_count} product photos synced"},
                status=201
            )

        except Exception as e:
            return Response({"error": str(e)}, status=500)






class UploadAccSalesTypesAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list"}, status=400)

        try:
            AccSalesTypes.objects.filter(client_id=client_id).delete()

            for item in data:
                AccSalesTypes.objects.create(
                    name=item.get('name'),
                    goddown=item.get('goddown'),
                    user=item.get('user'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} acc_sales_types uploaded"}, status=201)

        except Exception as e:
            logger.error(f"Error in UploadAccSalesTypesAPI: {e}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccSalesTypesAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        rows = AccSalesTypes.objects.filter(client_id=client_id)

        data = [{
            "name": r.name,
            "goddown": r.goddown,
            "user": r.user
        } for r in rows]

        return Response({"count": len(data), "acc_sales_types": data}, status=200)



class UploadAccGoddownAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            AccGoddown.objects.filter(client_id=client_id).delete()

            for item in data:
                AccGoddown.objects.create(
                    goddownid=item['goddownid'],
                    name=item['name'],
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} goddowns uploaded"}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)




class GetAccGoddownAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        rows = AccGoddown.objects.filter(client_id=client_id)

        data = [{
            "goddownid": r.goddownid,
            "name": r.name,
        } for r in rows]

        return Response({"count": len(data), "acc_goddown": data}, status=200)





class UploadAccGoddownStockAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            AccGoddownStock.objects.filter(client_id=client_id).delete()

            for item in data:
                AccGoddownStock.objects.create(
                    goddownid=item['goddownid'],
                    product=item['product'],
                    quantity=item.get('quantity'),
                    barcode=item.get('barcode'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} goddownstock rows uploaded"}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)





class GetAccGoddownStockAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        rows = AccGoddownStock.objects.filter(client_id=client_id)

        data = [{
            "goddownid": r.goddownid,
            "product": r.product,
            "quantity": str(r.quantity) if r.quantity else None,
            "barcode": r.barcode
        } for r in rows]

        return Response({"count": len(data), "acc_goddownstock": data}, status=200)



class UploadAccDepartmentsAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            AccDepartments.objects.filter(client_id=client_id).delete()

            for item in data:
                AccDepartments.objects.create(
                    department_id=item['department_id'],
                    department=item['department'],
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} departments uploaded"}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class GetAccDepartmentsAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get("client_id")

        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        rows = AccDepartments.objects.filter(client_id=client_id)

        data = [{
            "department_id": r.department_id,
            "department": r.department,
        } for r in rows]

        return Response({"count": len(data), "acc_departments": data}, status=200)
