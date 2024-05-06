from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Respuesta
from .serializers import RespuestaSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    respuesta = Respuesta.objects.all()
    serializer = RespuestaSerializer(respuesta, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRespuesta(request, pk):
    respuesta = Respuesta.objects.get(id=pk)
    serializer = RespuestaSerializer(respuesta, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addRespuesta(request):
    serializer = RespuestaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateRespuesta(request, pk):
    respuesta = Respuesta.objects.get(id=pk)
    serializer = RespuestaSerializer(instance=respuesta, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteRespuesta(request, pk):
    respuesta = Respuesta.objects.get(id=pk)
    respuesta.delete()
    return Response('respuesta successfully deleted!')

