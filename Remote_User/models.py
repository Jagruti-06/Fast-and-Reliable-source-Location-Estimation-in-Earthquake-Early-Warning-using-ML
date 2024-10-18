from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class earthquake_early_warning_prediction(models.Model):

    ewtime= models.CharField(max_length=30000)
    latitude= models.CharField(max_length=30000)
    longitude= models.CharField(max_length=30000)
    depth= models.CharField(max_length=30000)
    mag= models.CharField(max_length=30000)
    magType= models.CharField(max_length=30000)
    nst= models.CharField(max_length=30000)
    gap= models.CharField(max_length=30000)
    dmin= models.CharField(max_length=30000)
    rms= models.CharField(max_length=30000)
    net= models.CharField(max_length=30000)
    idn= models.CharField(max_length=30000)
    updated= models.CharField(max_length=30000)
    place= models.CharField(max_length=30000)
    horizontalError= models.CharField(max_length=30000)
    depthError= models.CharField(max_length=30000)
    magError= models.CharField(max_length=30000)
    magNst= models.CharField(max_length=30000)
    Prediction= models.CharField(max_length=30000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



