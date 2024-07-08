from django.db import models
from django.utils import timezone

# Create your models here.
class SoilMOistureReading(models.Model):
    timestamp = models.DateTimeField(Default=timezone.now)
    soil_moisture_percentage = models.FloatField()

    def _str_(self):
        return f"{self.timestamp} - {self.soil_level}"
