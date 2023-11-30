from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


class CourseViewSet(APIView):
    def get(self, request, *args, **kwargs):
        pass


class SkillViewSet(viewsets.ModelViewSet):
    pass


class SelectionViewSet(APIView):
    def get(self, request, *args, **kwargs):
        pass


class UserViewSet(viewsets.ModelViewSet):
    pass
