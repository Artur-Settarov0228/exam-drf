from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'siz admin emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_admin


class IsDoctor(BasePermission):
    message = 'siz doctor emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_doctor

class IsPatient(BasePermission):
    message = 'siz patient emassiz'

    def has_permission(self, request, view):
        return request.user and request.user.is_patient
    
class IsOwner(BasePermission):
    message = 'sizga bu tizimga kira olmaysiz'

    def has_object_permission(self, request, view, obj):
        
        if request.user.is_admin:
            return True
        
        if request.user.is_doctor:
            return obj.doctor == request.user
        
        if request.user.is_patient:
            return obj.patient == request.user
        
        return False