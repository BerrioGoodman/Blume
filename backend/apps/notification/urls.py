from django.urls import path
from .views import NotificationViewSet

urlpatterns = [
    path("lista/", NotificationViewSet.as_view({'get': 'list'}), name="notificaciones-lista"),
    path("crear/", NotificationViewSet.as_view({'post': 'create'}), name="notificaciones-crear"),
    path("<int:pk>/detalle/", NotificationViewSet.as_view({'get': 'retrieve'}), name="notificaciones-detalle"),
    path("<int:pk>/actualizar/", NotificationViewSet.as_view({'put': 'update', 'patch': 'partial_update'}), name="notificaciones-actualizar"),
    path("<int:pk>/eliminar/", NotificationViewSet.as_view({'delete': 'destroy'}), name="notificaciones-eliminar"),
]