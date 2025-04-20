from rest_framework import serializers
import core.models as models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'role', 'password')
        extra_kwargs = {
            'password':{'write_only':True},
        }
    
    def validate_role(self, role):
        allowed = ['student', 'teacher']
        if role not in allowed:
            raise serializers.ValidationError("You can choose only two roles: teacher and student")
        return role

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.User(**validated_data)
        user.set_password(password)
        user.save()
        return user