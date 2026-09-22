from django.contrib import admin
from django.urls import path,include
from academy.routers import router as academy_router
api_patterns=[
path('students/',include(academy_router.urls)),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(api_patterns))
]
