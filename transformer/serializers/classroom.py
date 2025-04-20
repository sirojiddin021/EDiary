from rest_framework import serializers
import core.models as models


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classroom
        fields = '__all__'