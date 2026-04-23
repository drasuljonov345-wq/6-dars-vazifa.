from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet, RegisterView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]
