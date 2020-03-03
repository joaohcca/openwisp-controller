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
        
	#track manual changes to deviceip (usefull to avoid conflict with non-openwisp-devices such as gateways, dns and other servers on same subnet) 
           
    if created:
            
        #request new ip based on org subnet (retrieve org and subnet first)
            
        #request new ip based on org subnet (using request.get and subnet API) 

        #save ip to device config (either setting context variable or editing device network interface with same same as subnet)

        #save changes to the subnet  
            
    pass

@receiver(post_delete, sender=Device)
def device_deleted_receiver(sender, instance, **kwargs):
    #Make device's IP available again, update orgnization subnet 
    pass

