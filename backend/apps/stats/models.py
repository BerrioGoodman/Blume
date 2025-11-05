from django.db import models

# Create your models here.

class StatisticsModel(models.Model):
    total_students = models.IntegerField(default=0)
    total_companies = models.IntegerField(default=0)
    total_vacancies = models.IntegerField(default=0)
    total_applications = models.IntegerField(default=0)
    total_accepted_applications = models.IntegerField(default=0)
    total_rejected_applications = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Statistics"

    def __str__(self):
        return f"Statistics - Students: {self.total_students}, Companies: {self.total_companies}, Vacancies: {self.total_vacancies}, Applications: {self.total_applications}"
