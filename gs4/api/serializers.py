from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
# with serializers
# class StudentSerializers(serializers.Serializer):
#     id  = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length = 100)
#     age = serializers.IntegerField()
#     city = serializers.CharField(max_length = 100)

#     class Meta:
#         ordering = ['id']

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance


# with model serializer
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Student
        fields = ['url','id', 'name', 'age', 'city', 'owner']

class UserSerializers(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(many=True, view_name='student-detail', read_only=True)
    class Meta:
        model = User
        fields  = ['url','id', 'username','students']