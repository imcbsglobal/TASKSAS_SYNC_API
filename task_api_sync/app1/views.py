from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccUsers, Misel, AccMaster, AccLedgers, AccInvmast,CashAndBankAccMaster,AccTtServicemaster


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
            # Only delete existing data if not appending
            if not append:
                AccMaster.objects.filter(client_id=client_id).delete()

            for item in data:
                # Use get_or_create or update_or_create to handle duplicates
                acc_master, created = AccMaster.objects.update_or_create(
                    code=item['code'],
                    client_id=client_id,
                    defaults={
                        'name': item.get('name'),
                        'opening_balance': item.get('opening_balance'),
                        'debit': item.get('debit'),
                        'credit': item.get('credit'),
                        'place': item.get('place'),
                        'phone2': item.get('phone2'),
                        'openingdepartment': item.get('openingdepartment'),
                        'area': item.get('area') if item.get('area') else None,
                    }
                )

            action = "appended" if append else "uploaded (old data cleared)"
            return Response({"message": f"{len(data)} acc_master records {action} for client_id {client_id}."}, status=201)

        except Exception as e:
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
            "opening_balance": str(m.opening_balance) if m.opening_balance is not None else None,
            "debit": str(m.debit) if m.debit is not None else None,
            "credit": str(m.credit) if m.credit is not None else None,
            "place": m.place,
            "phone2": m.phone2,
            "openingdepartment": m.openingdepartment,
            "area": m.area if m.area else ""  # ensure area always included
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
            # Only delete existing data if not appending
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
                    client_id=client_id
                )

            action = "appended" if append else "uploaded (old data cleared)"
            return Response({"message": f"{len(data)} acc_ledgers records {action} for client_id {client_id}."}, status=201)

        except Exception as e:
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
            "narration": l.narration
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
    
class UploadCashAndBankAccMasterAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of cashandbankaccmaster items."}, status=400)

        try:
            # Delete existing records for this client_id
            CashAndBankAccMaster.objects.filter(client_id=client_id).delete()

            for item in data:
                CashAndBankAccMaster.objects.create(
                    code=item['code'],
                    name=item['name'],
                    super_code=item.get('super_code'),
                    opening_balance=item.get('opening_balance'),
                    opening_date=item.get('opening_date'),
                    debit=item.get('debit'),
                    credit=item.get('credit'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} cashandbankaccmaster records uploaded for client_id {client_id}."}, status=201)

        except Exception as e:
            return Response({"error": str(e)}, status=500)


class GetCashAndBankAccMasterAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        cashandbankaccmaster = CashAndBankAccMaster.objects.filter(client_id=client_id)
        data = [{
            "code": m.code,
            "name": m.name,
            "super_code": m.super_code,
            "opening_balance": str(m.opening_balance) if m.opening_balance else None,
            "opening_date": m.opening_date.strftime('%Y-%m-%d') if m.opening_date else None,
            "debit": str(m.debit) if m.debit else None,
            "credit": str(m.credit) if m.credit else None,
        } for m in cashandbankaccmaster]

        return Response({"count": len(data), "cashandbankaccmaster": data}, status=200)
    


class UploadAccTtServicemasterAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')
        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)
        if not isinstance(data, list):
            return Response({"error": "Expected list"}, status=400)

        try:
            AccTtServicemaster.objects.filter(client_id=client_id).delete()
            for row in data:
                AccTtServicemaster.objects.create(
                    slno=row['slno'],
                    type=row.get('type'),
                    code=row.get('code'),
                    name=row.get('name'),
                    client_id=client_id
                )
            return Response({"message": f"{len(data)} acc_tt_servicemaster rows uploaded"}, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class GetAccTtServicemasterAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')
        if not client_id:
            return Response({"error": "Missing client_id"}, status=400)

        rows = AccTtServicemaster.objects.filter(client_id=client_id)
        data = [{"slno": r.slno, "type": r.type, "code": r.code, "name": r.name} for r in rows]
        return Response({"count": len(data), "acc_tt_servicemaster": data}, status=200)

# GET http://127.0.0.1:8000/api/get-users/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-misel/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-master/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-ledgers/?client_id=CLIENT001
# GET http://127.0.0.1:8000/api/get-acc-invmast/?client_id=CLIENT001
