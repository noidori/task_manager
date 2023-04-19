from django.db import models
from .user import User


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        NEW = "new"
        IN_DEVELOPMENT = "in_development"
        IN_QA = "in_qa"
        IN_CODE_REVIEW = "in_code_review"
        READY_FOR_RELEASE = "ready_for_release"
        RELEASED = "released"
        ARCHIVED = "archived"

    class TaskPriority(models.TextChoices):
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        URGENT = 4

    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=255, choices=TaskStatus.choices, default=TaskStatus.NEW
    )
    priority = models.CharField(
        max_length=255, choices=TaskPriority.choices, default=TaskPriority.MEDIUM
    )
    author = models.ForeignKey(
        User, related_name="created_tasks", on_delete=models.CASCADE
    )
    performer = models.ForeignKey(
        User,
        related_name="assigned_tasks",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["-priority", "due_date"]),
        ]

    def __str__(self):
        return self.title
