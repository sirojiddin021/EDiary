from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
import core.models as models
import transformer.serializers as sers


class RegisterAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = sers.UserSerializer


class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = sers.UserSerializer

    def get_object(self):
        return self.request.user