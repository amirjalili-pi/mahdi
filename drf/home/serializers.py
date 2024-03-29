from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    car = serializers.SlugRelatedField(slug_field='year', read_only=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email', 'car')
        extra_kwargs = {
            'email': {'write_only': True}
        }

    def validate_name(self, value):
        if 'admin' in value.lower():
            raise serializers.ValidationError('name cant be admin')
        return value
