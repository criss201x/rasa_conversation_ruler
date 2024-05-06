from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MensajeRespuesta
from .serializers import MensajeRespuestaSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    mensajeRespuesta = MensajeRespuesta.objects.all()
    serializer = MensajeRespuestaSerializer(mensajeRespuesta, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMensajeRespuesta(request, pk):
    mensajeRespuesta = MensajeRespuesta.objects.get(id=pk)
    serializer = MensajeRespuestaSerializer(mensajeRespuesta, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addMensajeRespuesta(request):
    serializer = MensajeRespuestaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateMensajeRespuesta(request, pk):
    mensajeRespuesta = MensajeRespuesta.objects.get(id=pk)
    serializer = MensajeRespuestaSerializer(instance=mensajeRespuesta, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteMensajeRespuesta(request, pk):
    mensajeRespuesta = MensajeRespuesta.objects.get(id=pk)
    mensajeRespuesta.delete()
    return Response('mensaje respuesta successfully deleted!')

