from django.urls import include, path
from rest_framework import routers
from .views import ContatoView

router = routers.DefaultRouter()
router.register(r'contato', ContatoView)

urlpatterns = [
    path('', include(router.urls))
]