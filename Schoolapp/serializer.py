from rest_framework import serializers
from Schoolapp.models import Student

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('Name', 'div', 'address', 'phone_number')