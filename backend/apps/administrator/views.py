from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import AministratorModel
from .serializers import AdministratorSerializer, AdministratorRegistroSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = AministratorModel.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None  # Disable pagination for list

    def get_queryset(self):
        # For educational purposes, allow listing all administrators
        return AministratorModel.objects.all()

class AdministratorProfileViewSet(viewsets.ModelViewSet):
    queryset = AministratorModel.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None  # Disable pagination for profile

    def get_queryset(self):
        return AministratorModel.objects.filter(user=self.request.user)

    def get_object(self):
        # For profile endpoints, return the user's admin instance
        return self.get_queryset().first()

class RegistrarAdministratorAPI(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(
        request=AdministratorRegistroSerializer,
        responses={"201": AdministratorRegistroSerializer},
        auth=[]
    )
    def create(self, request):
        serializer = AdministratorRegistroSerializer(data=request.data)
        if serializer.is_valid():
            administrator = serializer.save()
            return Response({
                "id": administrator.id,
                "username": administrator.user.username,
                "email": administrator.user.email,
                "nombre": f"{administrator.user.first_name} {administrator.user.last_name}",
                "rol": administrator.rol,
                "nivel_acceso": administrator.nivel_acceso
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
