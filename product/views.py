from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from product.serializers import ConversionSerializer, ConversionResponseSerializer
from product.utils.parse_base64_to_ascii import base64_to_ascii

class ConversionViewSet(viewsets.GenericViewSet):

    serializer_class=ConversionSerializer

    @extend_schema(request=ConversionSerializer, responses=ConversionResponseSerializer)
    @action(detail=False, methods=['post'])
    def convert(self, request):
        conversion = ConversionSerializer(data=request.data)

        if not conversion.is_valid():
            return Response(conversion.errors, status=status.HTTP_400_BAD_REQUEST)

        result = base64_to_ascii(conversion.data['base_64'], conversion.data['size'])

        if hasattr(result, 'error'):
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
        ascii_art = result['ascii_art']

        return Response({'ascii_art': ascii_art}, status=status.HTTP_201_CREATED)
