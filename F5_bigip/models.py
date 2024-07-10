from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.db.models.functions import Lower
from utilities.querysets import RestrictedQuerySet


from netbox.models import NetBoxModel

from .choices import *

class Node(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    ipaddress_id = models.OneToOneField(
                                            to = 'ipam.IPAddress',
                                            on_delete = models.CASCADE,
                                            null = False,
                                            blank = False
    )
    description = models.CharField(
        "Description",
        max_length=200,
        blank=True
    )
    partition_id = models.ForeignKey(
        to='Partition',
        on_delete = models.CASCADE,
        related_name="nodes",
        verbose_name="Partition",
        null = False,
        blank = False
    )

    objects = RestrictedQuerySet.as_manager()

    class Meta:
        ordering = ["name"]
        verbose_name = 'Node'
        verbose_name_plural = 'Nodes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:node", args=[self.pk])

###POOL###

class Pool(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    allownat = models.CharField(
        "Allow NAT",
        max_length=200,
        choices=PoolAllowChoices,
        default=PoolAllowChoices.CHOICE_YES,
        blank=True
    )
    allowsnat = models.CharField(
        "Allow SNAT",
        max_length=200,
        choices=PoolAllowChoices,
        default=PoolAllowChoices.CHOICE_YES,
        blank=True
    )
    load_balancing_mode = models.CharField(
        "Load-Balancing Mode",
        max_length=200,
        choices=PoolBalancingChoices,
        default=PoolBalancingChoices.LOADBALANCING_1
    )
    description = models.CharField(
        "Description",
        max_length=200,
        blank=True
    )
    partition_id = models.ForeignKey(to='Partition', on_delete = models.CASCADE, null=False, blank = False)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Pool'
        verbose_name_plural = 'Pools'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:pool", args=[self.pk])



class PoolMember(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    node_id = models.ForeignKey(to='Node', on_delete = models.CASCADE, null=True, blank = True, related_name = "pools")
    port = models.CharField(
        "Porta",
        max_length=65535,
    )
    pool_id = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True, related_name = "members")
    state = models.CharField(
        "State",
        max_length=200,
        choices=StateChoices,
        default=StateChoices.STATE_ENABLED
    )
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:poolmember", args=[self.pk])

class Irule(models.Model):
    name = models.CharField(
        max_length=200
    )
    partition_id = models.ForeignKey(to='Partition', on_delete = models.CASCADE, null=False, blank = False)
    definition = models.TextField(blank=False,)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Irule'
        verbose_name_plural = 'Irules'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:irule", args=[self.pk])

##VIRTUAL SERVER###

class VirtualServer(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    description = models.CharField(
        "Description",
        max_length=200,
        blank=True
    )
    #mask = models.IntegerField(default=0)
    source_address = models.CharField(
        "Source Address",
    )
    state = models.CharField(
        "State",
        max_length=200,
        choices=StateChoices,
        default=StateChoices.STATE_ENABLED
    )
    port = models.CharField(
        "Port",
        max_length=65535,
    )
    VS_type = models.CharField(
        "Type",
        max_length=200,
        choices=VirtServerChoices,
        default=VirtServerChoices.VIRTUALSERVER_1
    )
    pool_id = models.ForeignKey(to='Pool', on_delete = models.SET_NULL, null=True, blank = True)
    virtualaddress_id = models.ForeignKey(to='VirtualAddress', on_delete = models.CASCADE, null=True, blank = True)
    partition_id = models.ForeignKey(to='Partition', on_delete = models.CASCADE, null=False, blank = False)
    irules = models.ManyToManyField(
        to="Irule",
        related_name="virtual_servers",
        blank=True,
    )
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Virtual Server'
        verbose_name_plural = 'Virtual Servers'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:virtualserver", args=[self.pk])



class VirtualAddress(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    ipaddress_id = models.ForeignKey(to = 'ipam.IPAddress', on_delete=models.CASCADE, null=True, blank=True)
    partition_id = models.ForeignKey(to='Partition', on_delete = models.CASCADE, null=False, blank = False)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["ipaddress_id"]
        verbose_name = 'Virtual Address'
        verbose_name_plural = 'Virtual Addresses'
    def __str__(self):
        return self.ipaddress_id
    
    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:virtualaddress", args=[self.pk])
    


class Clusterf5(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Cluster'
        verbose_name_plural = 'Clusters'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:clusterf5")


class Partition(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    devicef5_id = models.ForeignKey(to = 'Devicef5', on_delete=models.CASCADE, null=False, blank=False)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Partition'
        verbose_name_plural = 'Partitions'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:partition", args=[self.pk])

class Devicef5(models.Model):
    name = models.CharField(
        "Name",
        max_length=200
    )
    device_id = models.ForeignKey(to = 'dcim.Device', on_delete=models.CASCADE, null=False, blank=False)
    clusterf5_id = models.ForeignKey(to = 'Clusterf5', on_delete=models.SET_NULL, null=True, blank=True)
    objects = RestrictedQuerySet.as_manager()
    class Meta:
        ordering = ["name"]
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:F5_bigip:devicef5", args=[self.pk])