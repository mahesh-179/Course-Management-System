from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    age = models.SmallIntegerField(blank=True,null=True)
    address = models.TextField()
    created_date = models.DateField(auto_now=True)


    def __str__(self):
        return f"{self.name.upper()}"

class Course(models.Model):
    course_name = models.CharField(max_length=25,blank=True,null=True)
    description = models.TextField()
    duration = models.DateField()
    fee = models.DecimalField(max_digits=10,decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.course_name}"

class Enrollment(models.Model):
    class Status(models.TextChoices):
        JOINED = 'Joined', 'Joined'
        COMPLETED = 'Completed', 'Completed'
        DROPPED = 'Dropped', 'Dropped'

    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrollments') #student.enrollments.all()
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments') #student.course.all()
    enrollment_date = models.DateField(auto_now=True)
    status = models.CharField(
    max_length=20,
    choices=Status.choices,
    default=Status.JOINED
)
    
