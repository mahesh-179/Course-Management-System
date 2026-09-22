from rest_framework import serializers
from .models import Student,Course,Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.HyperlinkedRelatedField(many=False,read_only=True,view_name='student-detail')
    course = serializers.HyperlinkedRelatedField(many=False,read_only=True,view_name ='course-detail')
    class Meta:
        model = Enrollment
        fields = ['id','student','course','enrollment_date','status']