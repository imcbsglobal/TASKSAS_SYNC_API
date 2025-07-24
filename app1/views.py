from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccUsers
import traceback

class UploadAccUsersAPI(APIView):
    def post(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({"error": "Expected a list of user items."}, status=400)

        try:
            # Delete all existing records
            AccUsers.objects.all().delete()

            # Insert new records
            for idx, item in enumerate(data):
                try:
                    print(f"Inserting record {idx + 1}: {item}")
                    AccUsers.objects.create(
                        id=item['id'],
                        pass_field=item['pass'],
                        role=item.get('role'),
                        accountcode=item.get('accountcode'),
                    )
                except Exception as inner_e:
                    print(f"❌ Error inserting record {idx + 1}: {item}")
                    print(traceback.format_exc())
                    raise inner_e

            return Response(
                {"message": f"Data cleared and {len(data)} user records added."},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            print(traceback.format_exc())
            return Response({"error": f"Server error: {str(e)}"}, status=500)


class GetAccUsersAPI(APIView):
    def get(self, request):
        try:
            users = AccUsers.objects.all()
            user_data = [
                {
                    "id": user.id,
                    "pass": user.pass_field,
                    "role": user.role,
                    "accountcode": user.accountcode
                }
                for user in users
            ]
            return Response({"count": len(user_data), "users": user_data}, status=200)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)
        







from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Misel
from .serializers import MiselSerializer
import traceback

class UploadMiselAPI(APIView):
    def post(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({"error": "Expected a list of misel items."}, status=400)

        try:
            # Delete all existing records
            Misel.objects.all().delete()

            # Insert new records
            for idx, item in enumerate(data):
                try:
                    print(f"Inserting record {idx + 1}: {item}")
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
                    )
                except Exception as inner_e:
                    print(f"❌ Error inserting record {idx + 1}: {item}")
                    print(traceback.format_exc())
                    raise inner_e

            return Response(
                {"message": f"Data cleared and {len(data)} misel records added."},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            print(traceback.format_exc())
            return Response({"error": f"Server error: {str(e)}"}, status=500)


class GetMiselAPI(APIView):
    def get(self, request):
        try:
            misel = Misel.objects.all()
            misel_data = [
                {
                    "firm_name": m.firm_name,
                    "address": m.address,
                    "phones": m.phones,
                    "mobile": m.mobile,
                    "address1": m.address1,
                    "address2": m.address2,
                    "address3": m.address3,
                    "pagers": m.pagers,
                    "tinno": m.tinno
                }
                for m in misel
            ]
            return Response({"count": len(misel_data), "misel": misel_data}, status=200)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)