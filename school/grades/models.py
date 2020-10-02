from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'students'

    def media(self):
        notas = self.grade_set.all()
        nota1 = notas[0].value
        nota2 = notas[1].value
        nota3 = notas[2].value

        media = (nota1 + nota2 + nota3) / len(notas)
        return float("{:.1f}".format(media))


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        db_table = 'grades'
