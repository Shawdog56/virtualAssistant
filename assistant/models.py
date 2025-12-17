from django.db import models
from django.contrib.auth.models import User

### Settings
class EntSettingsAccount(models.Model):
    imgPath = models.CharField(max_length=255, blank=True, null=True)
    userId = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    

### Commands
class CatCommandType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class EntExecutedCommand(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    commandType = models.ForeignKey(
        CatCommandType,
        on_delete=models.CASCADE
    )
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


## Topics
class CatTopicType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class EntTopic(models.Model):
    url = models.CharField(max_length=100, null=False, unique=True)
    topicTypeId = models.ForeignKey(
        CatTopicType,
        on_delete=models.CASCADE,
        null=False
    )
    deviceId = models.OneToOneField(
        'EntDevice',
        on_delete=models.CASCADE,
        null=False,
        related_name='topic'
    )


### Devices
class CatDeviceType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class CatUbicationDeviceType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)


class EntDevice(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    deviceTypeId = models.ForeignKey(
        CatDeviceType,
        on_delete=models.CASCADE
    )
    ubicationTypeId = models.ForeignKey(
        CatUbicationDeviceType,
        on_delete=models.CASCADE
    )


class DeviceActivityLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)
    deviceTypeId = models.ForeignKey(
        EntDevice,
        on_delete=models.CASCADE
    )

