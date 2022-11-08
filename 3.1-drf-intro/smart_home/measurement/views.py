from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer, MeasurementDetailSerializer


class SensorsAPICreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorAPIUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPICreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDetailSerializer
