from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class Guitar(models.Model): #гитара
    brand= models.CharField(max_length=70, blank=False, default='') #fender , martin , yamaha,Gibson
    type = models.CharField(max_length=70,blank = False,default='' ) #acoustic, electric, bass guitar , semi-acoustics, classic
    quantity_string = models.IntegerField(blank=False)# 6 or 12 
    hull_shape= models.CharField(max_length=50, blank=False, default='') # stratocaster, telecaster,Superstrat,Warlock
    color= models.CharField(max_length=40, blank=False, default='')
    availability= models.BooleanField(default=False)
    image = models.CharField(max_length=255, null=True)
    price= models.FloatField(blank=False)
  

class Amplifier(models.Model): #усилитель 
    brand= models.CharField(max_length=70, blank=False, default='') #Fender , Marshall , Yamaha ,PRINCETON, VOX
    type = models.CharField(max_length=70,blank = False,default='' ) # Транзисторные усилители, Цифровые усилители
    color= models.CharField(max_length=40, blank=False, default='')
    image = models.CharField(max_length=255, null=True)
    price= models.FloatField(blank=False)


class Pick(models.Model): #медиатор
    image = models.CharField(max_length=255, null=True)
    brand= models.CharField(max_length=70, blank=False, default='')
    thickness= models.FloatField(blank=False) #толщина
    color= models.CharField(max_length=40, blank=False, default='')
    price= models.FloatField(blank=False)


class Capo(models.Model): #каподастры
    image = models.CharField(max_length=255, null=True)
    brand= models.CharField(max_length=70, blank=False, default='')# alice 
    type = models.CharField(max_length=70,blank = False,default='' ) # Пружинный , Замковый,Винтовой
    color= models.CharField(max_length=40, blank=False, default='')
    price= models.FloatField(blank=False)


class User(AbstractUser):
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.CharField(max_length=90, blank=False, unique=True)
    username = models.CharField(max_length=90, blank=True, null=True, unique=True)
    password = models.CharField(max_length=90, blank=False)    
    REQUIRED_FIELDS = []     


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)



    












