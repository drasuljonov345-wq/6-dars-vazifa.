from rest_framework import serializers
from .models import *
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Kategoriya nomining bosh harfi katta bo'lishi kerak!")

        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("Kategoriya nomi faqat harflardan tashkil topgan bo'lishi kerak!")

        return value


class CategoryAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_year', 'price', 'category')
        read_only_fields = ('id',)

    def validate_title(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Kitob nomining bosh harfi katta bo'lishi kerak!")
        return value

    def validate_author(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Muallif ismining bosh harfi katta bo'lishi kerak!")

        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("Muallif ismi faqat harflardan tashkil topgan bo'lishi kerak!")

        return value

    def validate_published_year(self, value):
        hozirgi_yil = datetime.now().year
        if not (value.year > hozirgi_yil - 500 and value.year <= hozirgi_yil):
            raise serializers.ValidationError("Kitob 500 yildan eski bo'lmasligi kerak!")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx musbat son bo'lishi kerak!")

        if value > 999999999:
            raise serializers.ValidationError("Narx juda baland. Iltimos, qayta tekshiring.")

        return value


class BookAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_year', 'price', 'category')
        read_only_fields = ('id',)
