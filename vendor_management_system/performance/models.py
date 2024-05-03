from django.db import models
from vendors.models import Vendor
from django.utils import timezone

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def calculate_on_time_delivery_rate(self):
        print("purchase order  calculate_on_time_delivery_rate call..")
        completed_pos = self.vendor.purchaseorder_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        on_time_pos = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date')).count()
        self.on_time_delivery_rate = (on_time_pos / total_completed_pos) * 100 if total_completed_pos > 0 else 0.0

    def calculate_quality_rating_avg(self):
        print("purchase order  calculate_quality_rating_avg call..")
        completed_pos = self.vendor.purchaseorder_set.filter(status='completed').exclude(quality_rating=None)
        total_completed_pos = completed_pos.count()
        total_quality_rating = completed_pos.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
        self.quality_rating_avg = total_quality_rating if total_quality_rating else 0.0

    def calculate_average_response_time(self):
        print("purchase order  calculate_average_response_time call..")

        completed_pos = self.vendor.purchaseorder_set.filter(status='completed').exclude(acknowledgment_date=None)
        total_completed_pos = completed_pos.count()
        total_response_time = sum((po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_pos)
        self.average_response_time = total_response_time / total_completed_pos if total_completed_pos > 0 else 0.0

    def calculate_fulfillment_rate(self):
        print("purchase order  calculate_fulfillment_rate call..")
        total_pos = self.vendor.purchaseorder_set.count()
        successful_pos = self.vendor.purchaseorder_set.filter(status='completed').exclude(quality_rating=None)
        self.fulfillment_rate = (successful_pos.count() / total_pos) * 100 if total_pos > 0 else 0.0

    def save(self, *args, **kwargs):
        self.calculate_on_time_delivery_rate()
        self.calculate_quality_rating_avg()
        self.calculate_average_response_time()
        self.calculate_fulfillment_rate()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.vendor.name}_Historical Performance"
