from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.services import sac, price
from .serializers import SacSerializer, PriceSerializer


class SacView(APIView):
    def post(self, request, format=None):
        input_data = request.data
        sac_table = sac(
            input_data.get("loan"),
            input_data.get("installments_number"),
            input_data.get("interest"),
        )
        serializer = SacSerializer(data=sac_table, many=True)
        if serializer.is_valid():
            # Return the serialized SAC data as JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If serialization fails, return appropriate error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PriceView(APIView):
    def post(self, request, format=None):
        input_data = request.data
        price_table = price(
            input_data.get("loan"),
            input_data.get("installments_number"),
            input_data.get("interest"),
        )
        serializer = PriceSerializer(data=price_table, many=True)
        if serializer.is_valid():
            # Return the serialized SAC data as JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # If serialization fails, return appropriate error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
