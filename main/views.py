import django_filters
from rest_framework import viewsets
from main.models import Tag, Task, TaskStatus, User
from main.serializers import (
    UserSerializer,
    TaskSerializer,
    TagSerializer,
    TaskStatusSerializer,
)


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("name",)


class TaskFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(
        field_name="status__status", lookup_expr="icontains"
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__title", queryset=Tag.objects.all(), to_field_name="title"
    )
    assigned_to = django_filters.CharFilter(
        field_name="performer__username", lookup_expr="icontains"
    )
    created_by = django_filters.CharFilter(
        field_name="author__username", lookup_expr="icontains"
    )

    class Meta:
        model = Task
        fields = ["status", "tags", "assigned_to", "created_by"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id").select_related("author", "performer")
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().prefetch_related("tasks")
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = (
        Task.objects.all()
        .select_related("author", "performer")
        .prefetch_related("tags")
    )
    serializer_class = TaskSerializer


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
