from rest_framework import serializers
from .models import Student

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
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'city']