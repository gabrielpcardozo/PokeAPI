from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)  # evite usar `id` pq Django já cria um
    type = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.name} (#{self.number}, tipo: {self.type})"
    
    def pk_name(self):
        return self.name
