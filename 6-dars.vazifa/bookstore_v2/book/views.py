from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User

from .serializers import CategorySerializer, BookSerializer, RegisterSerializer
from .models import Category, Book
from .permissions import IsAdminOrReadOnly


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly]
