from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Categoria
from .serializers import CategoriaSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategoria(request, pk):
    categorias = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(categorias, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addCategoria(request):
    serializer = CategoriaSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def updateCategoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(instance=categoria, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteCategoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return Response('Categoria successfully deleted!')

