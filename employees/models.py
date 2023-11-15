from django.db import models




class Employee(models.Model):
    STATUS_CHOICE = [
        ("active", 'active'),
        ('deactive', 'deactive'),
    ]
    emp_name = models.CharField(max_length=255)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=12, decimal_places=3)
    status = models.CharField(max_length=9, choices=STATUS_CHOICE)

    def __str__(self):
        return self.emp_name


