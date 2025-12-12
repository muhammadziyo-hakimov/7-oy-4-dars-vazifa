from rest_framework import serializers
from .models import Category, Product, Course, Student

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    courses_ids = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Course.objects.all())

    def create(self, validated_data):
        courses_ids = validated_data.pop('courses_ids', [])
        student = Student.objects.create(**validated_data)
        student.courses.set(courses_ids)
        return student
    
    def update(self, instance, validated_data):
        courses_ids = validated_data.pop('courses_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if courses_ids is not None:
            instance.courses.set(courses_ids)
        instance.save()
        return instance
    


    class Meta:
        model = Student
        fields = "__all__"