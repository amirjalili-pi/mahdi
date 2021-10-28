from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .serializers import PersonSerializer
from .models import Person
from rest_framework import status


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'name': f'{name}'}, status=status.HTTP_200_OK)
    else:
        return Response({'name': 'Amirmahdi'}, status=status.HTTP_204_NO_CONTENT)

#
# @api_view()
# def show_persons(request):
#     persons = Person.objects.all()
#     ser_data = PersonSerializer(persons, many=True)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# @api_view()
# @permission_classes([IsAdminUser])
# def show_person(request, id):
#     try:
#         person = Person.objects.get(id=id)
#
#     except Person.DoesNotExist:
#
#         return Response({'Error': "the person doesNotExist"}, status=status.HTTP_404_NOT_FOUND)
#
#     ser_data = PersonSerializer(person)
#     return Response(ser_data.data, status=status.HTTP_200_OK)
#
#
# @api_view(['POST'])
# def create_person(request):
#     info = PersonSerializer(data=request.data)
#     if info.is_valid():
#         # Person(name=info.validated_data['name'], age=info.validated_data['age'],      ##doesnt need in modelSerializer
#         #        email=info.validated_data['email']).save()
#         info.save()
#         return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)
