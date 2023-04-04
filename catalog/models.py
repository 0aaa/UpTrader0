import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Menu ID')
    name = models.CharField(max_length=20, help_text='Menu name')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, help_text='Parent menu')
    class Meta:
        ordering = ['name']
    def get_absolute_url(self):
        return reverse('menu-details', args=[str(self.id)])
    def __str__(self):
        return self.name
    def print_parent(self):
        return self.parent