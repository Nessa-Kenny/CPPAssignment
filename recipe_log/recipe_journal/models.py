from django.db import models

# Create your models here.
class Add_Recipe(models.Model):
    """ADD Recipe option"""
    Title = models.CharField(max_length=200)
    #Measurement - metric imperial
    #Ingredients = models.TextField()
    #Method_Steps= models.TextField()
    #Notes = models.CharField(max_length=200)
    ##Photos / Image=models.
    #Keywords = models.CharField(max_length=200)
    #url?
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        """Return a string represention of the Model."""
        return self.text
        
class Entry(models.Model):
    """Details about the entries"""
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='entries'
    
    def __str__(self):
        """return string represented by the model"""
        return f"{self.text[50]}..."