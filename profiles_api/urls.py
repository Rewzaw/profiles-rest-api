from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # basename='profile' if we want do override queryset name

urlpatterns = [
    path('hello-apiview/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
