from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from .models import Person


@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'name': f'{name}'})
    else:
        return Response({'name': 'Amirmahdi'})


@api_view()
def show_persons(request):
    persons = Person.objects.all()
    ser_data = PersonSerializer(persons, many=True)
    return Response(ser_data.data)


@api_view()
def show_person(request, id):
    try:
        person = Person.objects.get(id=id)

    except Person.DoesNotExist:

        return Response({'Error': "the person doesNotExist"})

    ser_data = PersonSerializer(person)
    return Response(ser_data.data)
