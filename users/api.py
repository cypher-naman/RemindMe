from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .permissions import IsOwner

User = get_user_model()


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        Token.objects.filter(user=instance).delete()
