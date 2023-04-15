from rest_framework import serializers
from .models import Devices, Project, Template


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "idrandom",
            "name",
            "location",
            "description",
        )

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = (
            "id",
            "name",
            "location",
        )
    
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = (
            "id",
            "name",
            "sensor",
            "red",
            "descripcion",
        )