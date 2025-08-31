from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTeamLeadOrAdmin(BasePermission):
    """
    Sadece admin veya team_lead kullanıcıların kitap ekleme, güncelleme ve silme yetkisi var.
    Herkes kitapları görebilir (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request, view):
        # Güvenli metotlar (GET, HEAD, OPTIONS) herkes için izinli
        if request.method in SAFE_METHODS:
            return True

        # POST, PUT, DELETE için admin veya team_lead olmalı
        return request.user.is_authenticated and (
                request.user.is_superuser or getattr(request.user, 'role', None) == 'team_lead'
        )

    def has_object_permission(self, request, view, obj):
        # Güvenli metotlar (GET, HEAD, OPTIONS) herkes için izinli
        if request.method in SAFE_METHODS:
            return True

        # Obje üzerinde kontrol: admin veya team_lead
        return request.user.is_authenticated and (
                request.user.is_superuser or getattr(request.user, 'role', None) == 'team_lead'
        )


from rest_framework.permissions import BasePermission


class IsAdminUserRole(BasePermission):
    """
    Sadece admin rolündeki kullanıcıların erişimine izin verir.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
                request.user.is_superuser or request.user.role == 'admin'
        )
