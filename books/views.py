from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import PurchaseSerializer
from .models import Purchase



class PurchaseCreateView(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

