from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = 'siz admin emassiz'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsDoctor(BasePermission):
    message = 'siz doctor emassiz'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_doctor

class IsPatient(BasePermission):
    message = 'siz patient emassiz'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_patient
    
class IsOwner(BasePermission):
    message = 'sizga bu tizimga kira olmaysiz'

    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (request.user.is_admin or request.user.is_patient)
        
class IsdoctorOrPatient(BasePermission):
    message = 'sizga bu tizimga kira olmaysiz'

    def has_permission(self, request, view):
        return request.user and (request.user.is_doctor or request.user.is_patient)
    

