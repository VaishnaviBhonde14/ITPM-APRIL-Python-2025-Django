from django.db import models

# Create your models here.
class new_Student(models.Model):
    stuId = models.IntegerField()
    name = models.CharField(max_length=100)
    # age = models.IntegerField()
    email = models.EmailField(default='test@example.com')
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.name            