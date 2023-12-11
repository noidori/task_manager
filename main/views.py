from django.shortcuts import render
from rest_framework import viewsets
from main.serializers import (
    UserSerializer,
    TagSerializer,
    TaskSerializer,
    TaskStatusSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id").select_related("author",
                                                          "performer")
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().prefetch_related("tasks")
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().select_related("author",
                                                 "performer").prefetch_related(
        "tags")
    serializer_class = TaskSerializer


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
