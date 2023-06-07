from django.db import models
from django.db import models


class Grade(models.Model):
    value = models.IntegerField("Student grade")
    date = models.DateField("Grade date")
    course = models.ForeignKey("courses.course", on_delete=models.CASCADE, related_name='course', verbose_name="Course")
    student = models.ForeignKey("students.student", on_delete=models.CASCADE, related_name='student', verbose_name="Student")

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        
    def __str__(self):
        return f"{self.student} - {self.course}: {self.value}"
    