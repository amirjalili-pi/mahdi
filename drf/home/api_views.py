from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # def list(self, request):
    #     persons = Person.objects.all()
    #     serializer = PersonSerializer(persons, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     persons = Person.objects.all()
    #     person = get_object_or_404(persons, pk=pk)
    #     serializer = PersonSerializer(person)
    #     return Response(serializer.data)          # estephade as Viewset ha bayad method hara tarif kard
    #
    # def create(self, request):
    #     serializer = PersonSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'ok'})
    #     else:
    #         return Response(serializer.errors)
