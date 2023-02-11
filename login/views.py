from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# Create your views here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')

class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class =UserSerializer

    def get_object(self):
        return self.request.user
    