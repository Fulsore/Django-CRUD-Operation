from django.db import models

class StudentModel(models.Model):
    student_firstname = models.CharField(max_length=225)
    student_lastname = models.CharField(max_length=225)
    student_number = models.IntegerField()
    student_address = models.EmailField(max_length=225)
    student_fee = models.IntegerField()

    def __str__(self):
        return self.student_firstname
