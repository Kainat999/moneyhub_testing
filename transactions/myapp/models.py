from django.db import models

class Transaction(models.Model):
    client_id = models.CharField(max_length=255, null=False, default='missing')  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.description}"
