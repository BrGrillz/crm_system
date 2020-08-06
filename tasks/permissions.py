from django.http import Http404
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# class IsResponsibleOrOwnerPermission:
#     def has_permissions(self):
#         return self.request.user.id in self.get_object().responsible or self.get_object().author
#
#     def dispatch(self, request, *args, **kwargs):
#         if not self.has_permissions():
#             raise Http404()
#         return super().dispatch(request, *args, **kwargs)
#
#
# class IsRelated(IsResponsibleOrOwnerPermission):
#     def has_permissions(self):
#         return self.request.user.id in self.get_object().responsible or self.get_object().author or self.get_object().observer
