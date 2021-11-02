from django.db import models

# Create your models here.
class CommonFunction(models.Model):
    file = models.CharField(max_length=300)
    class_name = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    parameters = models.TextField(null=True, blank=True)
    usage = models.TextField(null=True, blank=True)
    return_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file+'-'+self.class_name+'-'+self.name