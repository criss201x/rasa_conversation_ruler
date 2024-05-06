from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mensajes
from .serializers import MensajeIntensionSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    mensajes = Mensajes.objects.all()
    serializer = MensajeIntensionSerializer(mensajes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMensajeIntension(request, pk):
    mensajes = Mensajes.objects.get(id=pk)
    serializer = MensajeIntensionSerializer(mensajes, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addMensajeIntension(request):
    serializer = MensajeIntensionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateMensajeIntension(request, pk):
    mensajes = Mensajes.objects.get(id=pk)
    serializer = MensajeIntensionSerializer(instance=mensajes, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMensajeIntension(request, pk):
    mensajes = Mensajes.objects.get(id=pk)
    mensajes.delete()
    return Response('mensaje successfully deleted!')

