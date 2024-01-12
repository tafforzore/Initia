# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PaymentSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class NotifyAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PaymentSerializer(data=data)

        if serializer.is_valid(): 
           data = {
                "status": serializer.data['status'],
                "ref_payment": serializer.data['ref_payment'],#reference du produit generrer par api
                "transaction_number": serializer.data['transaction_number'],
                "public_key": serializer.data['public_key'],
                "amount_received": serializer.data['amount_received'],
                "amount": serializer.data['amount'],
                "phone": serializer.data['phone'],
                "operator": serializer.data['operator'],
                "currency":serializer.data['currency'],
                "fees": serializer.data['fees'],
                "item_ref": serializer.data['item_ref'],
                "item_name": serializer.data['item_name'],
                "description": serializer.data['description'],
                "email": serializer.data['email'],
                "name": serializer.data['name'],
                "country": serializer.data['country'],
                "postal_code": serializer.data['postal_code'],
                "error_code": serializer.data['error_code'],
                "error_message": serializer.data['error_message'],
                "sign_token": serializer.data['sign_token'],
                "environement": serializer.data['environement']
            }
           
           if data["status"]=="Success":
               ##operation effectuer avec success
               print('operatitons effectuer avec success')
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url='login')
class apiMessage:
    def success(request):
        return render(request, 'notification/success.html')
    
    def cancel(request):
        return render(request, 'notification/cancel.html')