from django.db import models

# Create your models here.

class busstand(models.Model):
    city=models.CharField(max_length=30)
    code=models.CharField(max_length=3)

    def __str__(self):
        return f"{self.city} [{self.code}]"


class bus(models.Model):
    origin=models.ForeignKey(busstand , on_delete=models.CASCADE , related_name="start")
    destination=models.ForeignKey(busstand , on_delete=models.CASCADE , related_name="end")

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"


class p  assenger(models.Model):
    first=models.CharField(max_length=30)
    last=models.CharField(max_length=30)
    buses=models.ManyToManyField(bus,blank=True,related_name="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
        
    



    