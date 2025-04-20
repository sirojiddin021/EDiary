from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'
    

class IsAdminOrTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.user.role == 'teacher'
    

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher'
    

class IsTeacherOrStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'teacher' or request.user.role == 'student'
    

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'student'