from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import PurchaseSerializer
from .models import Purchase



class PurchaseCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


# class PurchaseCreateView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = PurchaseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def get(self, request, *args, **kwargs):
#         purchases = Purchase.objects.all()
#         serializer = PurchaseSerializer(purchases, many=True)
#         return Response(serializer.data)