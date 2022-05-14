from django.db import models

class siteModel(models.Model):
    
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.url