from rest_framework import serializers
import core.models as models


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Homework
        fields = '__all__'