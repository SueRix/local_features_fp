from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PetsModel, CareAndHealthModel
from .serializers import CareAndHealthSerializer, PetsSerializer


class PetsAPIView(APIView):
    def get(self, request):
        if request.method != 'GET':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        pets = PetsModel.objects.all()
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CareAndHealthAPIView(APIView):
    def get(self, request):
        if request.method != 'GET':
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        care_and_health_items = CareAndHealthModel.objects.all()
        serializer = CareAndHealthSerializer(care_and_health_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
