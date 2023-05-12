from django.db import models

# Create your models here.

    
class RentPurchaserDetails(models.Model):
    owner_name=models.CharField(max_length=300)
    buyer_name=models.CharField(max_length=300)
    district=models.CharField(max_length=300)
    division=models.CharField(max_length=300)
    rent_price=models.CharField(max_length=300)
    square_foot=models.CharField(max_length=300)
    washroom=models.CharField(max_length=300)
    bedroom=models.CharField(max_length=300)

    def __str__(self):
        return f"{self.id} {self.buyer_name}"
