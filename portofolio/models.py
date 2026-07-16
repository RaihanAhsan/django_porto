from django.db import models
from django.contrib.auth.models import User

class XenditTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)  # ID unik dari kita
    xendit_invoice_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.IntegerField()  # dalam Rupiah
    status = models.CharField(max_length=50, default='PENDING')  # PENDING, PAID, EXPIRED, FAILED
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    invoice_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.order_id} - {self.status}"