from django.urls import include, path
from rest_framework.routers import SimpleRouter

from account import views

router = SimpleRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]