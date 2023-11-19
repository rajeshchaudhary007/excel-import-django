from django.db import models

class Company(models.Model):
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    revenue_growth = models.CharField(max_length=100)
    employees = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Company"  
        verbose_name_plural = "Companies"  

    def __str__(self):
        return f'{self.name} {self.industry} {self.revenue}'


    @property
    def formatted_revenue(self):
        return '{:,}'.format(self.revenue)
    
   