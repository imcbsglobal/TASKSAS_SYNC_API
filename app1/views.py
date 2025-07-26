# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import AccUsers
# import traceback

# class UploadAccUsersAPI(APIView):
#     def post(self, request):
#         data = request.data
#         client_id = request.query_params.get('client_id')

#         if not client_id:
#             return Response({"error": "Missing client_id in query parameters."}, status=400)

#         if not isinstance(data, list):
#             return Response({"error": "Expected a list of user items."}, status=400)

#         try:
#             # Delete only the data for the given client_id
#             AccUsers.objects.filter(client_id=client_id).delete()

#             for idx, item in enumerate(data):
#                 AccUsers.objects.create(
#                     id=item['id'],
#                     pass_field=item['pass'],
#                     role=item.get('role'),
#                     accountcode=item.get('accountcode'),
#                     client_id=client_id
#                 )

#             return Response({"message": f"{len(data)} users uploaded for client_id {client_id}."}, status=201)

#         except Exception as e:
#             return Response({"error": str(e)}, status=500)


# class GetAccUsersAPI(APIView):
#     def get(self, request):
#         client_id = request.query_params.get('client_id')
#         if not client_id:
#             return Response({"error": "Missing client_id in query parameters."}, status=400)

#         users = AccUsers.objects.filter(client_id=client_id)
#         data = [{
#             "id": u.id,
#             "pass": u.pass_field,
#             "role": u.role,
#             "accountcode": u.accountcode,
#         } for u in users]

#         return Response({"count": len(data), "users": data}, status=200)

        







# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Misel
# from .serializers import MiselSerializer
# import traceback

# class UploadMiselAPI(APIView):
#     def post(self, request):
#         data = request.data
#         client_id = request.query_params.get('client_id')

#         if not client_id:
#             return Response({"error": "Missing client_id in query parameters."}, status=400)

#         if not isinstance(data, list):
#             return Response({"error": "Expected a list of misel items."}, status=400)

#         try:
#             Misel.objects.filter(client_id=client_id).delete()

#             for idx, item in enumerate(data):
#                 Misel.objects.create(
#                     firm_name=item.get('firm_name'),
#                     address=item.get('address'),
#                     phones=item.get('phones'),
#                     mobile=item.get('mobile'),
#                     address1=item.get('address1'),
#                     address2=item.get('address2'),
#                     address3=item.get('address3'),
#                     pagers=item.get('pagers'),
#                     tinno=item.get('tinno'),
#                     client_id=client_id
#                 )

#             return Response({"message": f"{len(data)} misel records uploaded for client_id {client_id}."}, status=201)

#         except Exception as e:
#             return Response({"error": str(e)}, status=500)


# class GetMiselAPI(APIView):
#     def get(self, request):
#         client_id = request.query_params.get('client_id')
#         if not client_id:
#             return Response({"error": "Missing client_id in query parameters."}, status=400)

#         misel = Misel.objects.filter(client_id=client_id)
#         data = [{
#             "firm_name": m.firm_name,
#             "address": m.address,
#             "phones": m.phones,
#             "mobile": m.mobile,
#             "address1": m.address1,
#             "address2": m.address2,
#             "address3": m.address3,
#             "pagers": m.pagers,
#             "tinno": m.tinno
#         } for m in misel]

#         return Response({"count": len(data), "misel": data}, status=200)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AccUsers, Misel


class UploadAccUsersAPI(APIView):
    def post(self, request):
        data = request.data
        client_id = request.query_params.get('client_id')

        if not client_id:
            return Response({"error": "Missing client_id in query parameters."}, status=400)

        if not isinstance(data, list):
            return Response({"error": "Expected a list of user items."}, status=400)

        try:
            # 🔁 Delete all acc_users entries for this client_id
            AccUsers.objects.filter(client_id=client_id).delete()

            # ✅ Insert new data
            for item in data:
                AccUsers.objects.create(
                    id=item['id'],
                    pass_field=item['pass'],
                    role=item.get('role'),
                    accountcode=item.get('accountcode'),
                    client_id=client_id
                )

            return Response({"message": f"{len(data)} users uploaded (old data cleared) for client_id {client_id}."}, status=201)

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
            # 🔁 Delete all misel entries for this client_id
            Misel.objects.filter(client_id=client_id).delete()

            # ✅ Insert new misel data
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
