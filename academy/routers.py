from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .viewsets import StudentViewSet,CourseViewSet,EnrollmentViewSet

router = DefaultRouter()
router.register('students',StudentViewSet)
router.register('course',CourseViewSet)    
router.register('enrollments',EnrollmentViewSet)