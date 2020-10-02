from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'students'

    @property
    def media(self):
        grades = self.grade_set.all()
        media = (grades[0].value + grades[1].value + grades[2].value) / len(grades)

        return float("{:.2f}".format(media))


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.FloatField()
