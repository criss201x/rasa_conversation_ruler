from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Intensiones
from .serializers import IntensionSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    intensiones = Intensiones.objects.all()
    serializer = IntensionSerializer(intensiones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIntension(request, pk):
    intensiones = Intensiones.objects.get(id=pk)
    serializer = IntensionSerializer(intensiones, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addIntension(request):
    serializer = IntensionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateIntension(request, pk):
    intensiones = Intensiones.objects.get(id=pk)
    serializer = IntensionSerializer(instance=intensiones, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteIntension(request, pk):
    intensiones = Intensiones.objects.get(id=pk)
    intensiones.delete()
    return Response('intension successfully deleted!')

