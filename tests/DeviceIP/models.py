from django.db import models
from openwisp_controller.config.models import Device
from openwisp_ipam.models import Subnet, IpAddress

class DeviceIP(models.Model):
    device_config = models.ForeignKey(Device, on_delete=models.CASCADE)
    ipaddr = models.ForeignKey(IpAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.device.name

    class Meta(AbstractConfig.Meta):
	unique_together = (
	('ipaddr', 'organization'),
	('device_config', 'organization'),
	)
        abstract = False


