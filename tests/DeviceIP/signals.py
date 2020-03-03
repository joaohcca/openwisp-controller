from django.apps import AppConfig
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save, post_delete
import requests
from openwisp_controller.config.models import Device
from openwisp_ipam.models import IpAddress, Subnet

@receiver(post_save, sender=Device)
def device_saved_receiver(sender, instance, created, **kwargs):
        
    if not created:
        #track changes to deviceip
            
        print("not created")
           
    if created:
            
        #request new ip based on org subnet
            
        #print("req_ip: ",req_ip)
            #request new ip based on org subnet

            #save ip to device config

            #update subnet
            
    pass

@receiver(post_delete, sender=Device)
def device_deleted_receiver(sender, instance, **kwargs):
   # may want to do something on delete
    pass

