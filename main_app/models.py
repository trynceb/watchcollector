from django.db import models

# Create your models here.
class Watch(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    metal = models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand + " " + self.model
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={"watch_id": self.id})
    
class Service(models.Model):
    date = models.DateField()
    
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_date_display()}'
    
    class Meta:
        ordering = ['-date']
