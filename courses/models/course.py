from django.db import models


class Course(models.Model):
    name = models.CharField("Course name", max_length=20)
    description = models.TextField("Description", max_length=255)
    duration = models.IntegerField("Course duration")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return f"Course {self.name} {self.phone}"

