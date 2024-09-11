from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    address = models.TextField(max_length=150)  
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, # One Specialization per Doctor
                                       on_delete=models.CASCADE)
    image = models.ImageField(default='default_doc.jpg', upload_to='profile_pics')
 
    
    def __str__(self):
        return self.name