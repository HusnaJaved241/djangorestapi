  
from django.db import models

# Create your models here.

class Students(models.Model):
    fullname = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE