from django.urls import path
from .views import SensorsAPICreate, SensorAPIUpdate, MeasurementAPICreate


urlpatterns = [
    path('sensors/', SensorsAPICreate.as_view()),
    path('sensors/<int:pk>/', SensorAPIUpdate.as_view()),
    path('measurement/', MeasurementAPICreate.as_view())
]
