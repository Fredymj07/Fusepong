from django.contrib import admin
from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class DocumentType(models.Model):
    name = models.CharField(max_length=24, null=False)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    document_number = models.CharField(max_length=40, null=False)
    phone =  models.CharField(max_length=14, null=False)
    email =  models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
        return self.name +  '  '  + self.last_name

class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')