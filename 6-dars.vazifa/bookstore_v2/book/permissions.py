from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Faqat admin foydalanuvchilar yozish, o'chirish va yangilash huquqiga ega.
    Oddiy autentifikatsiyadan o'tgan foydalanuvchilar faqat o'qiy oladi (GET).
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
