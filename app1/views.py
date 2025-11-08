from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccUsers, AccMaster
import traceback
import logging

logger = logging.getLogger(__name__)

# ------------------- USERS -------------------
class UploadAccUsersAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id."}, status=400)
        if not isinstance(data, list):
            return Response({"error": "Expected a list of users."}, status=400)

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
            return Response({"message": f"{len(data)} users uploaded for {client_id}."}, status=201)
        except Exception as e:
            logger.error(f"Error in UploadAccUsersAPI: {e}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccUsersAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')
        if not client_id:
            return Response({"error": "Missing client_id."}, status=400)

        users = AccUsers.objects.filter(client_id=client_id)
        data = [{
            "id": u.id,
            "pass": u.pass_field,
            "role": u.role,
            "accountcode": u.accountcode
        } for u in users]
        return Response({"count": len(data), "users": data}, status=200)

# ------------------- DEBTORS (AccMaster) -------------------
class UploadAccMasterAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')
        append = request.query_params.get('append', 'false').lower() == 'true'

        if not client_id:
            return Response({"error": "Missing client_id."}, status=400)
        if not isinstance(data, list):
            return Response({"error": "Expected a list of debtor records."}, status=400)

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
                        'place': item.get('place'),
                        'phone2': item.get('phone2'),
                        'openingdepartment': item.get('openingdepartment'),
                        'area': item.get('area')
                    }
                )
            return Response({"message": f"{len(data)} debtors uploaded for {client_id}."}, status=201)
        except Exception as e:
            logger.error(f"Error in UploadAccMasterAPI: {e}\n{traceback.format_exc()}")
            return Response({"error": str(e)}, status=500)


class GetAccMasterAPI(APIView):
    def get(self, request):
        client_id = request.query_params.get('client_id')
        if not client_id:
            return Response({"error": "Missing client_id."}, status=400)

        acc_master = AccMaster.objects.filter(client_id=client_id)
        data = [{
            "code": a.code,
            "name": a.name,
            "super_code": a.super_code,
            "opening_balance": str(a.opening_balance) if a.opening_balance else None,
            "debit": str(a.debit) if a.debit else None,
            "credit": str(a.credit) if a.credit else None,
            "place": a.place,
            "phone2": a.phone2,
            "openingdepartment": a.openingdepartment,
            "area": a.area
        } for a in acc_master]
        return Response({"count": len(data), "debtors": data}, status=200)
