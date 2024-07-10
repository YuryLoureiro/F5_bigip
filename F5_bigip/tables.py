import django_tables2 as tables
from django_tables2.utils import Accessor

from netbox.tables import NetBoxTable, columns
from django.db.models import Count
from . import models

class NodeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    #pk = columns.ToggleColumn()
    #name = tables.LinkColumn("plugins:F5_bigip:node", args=[A("pk")], verbose_name = "Nome")
    ipaddress_id = tables.Column(verbose_name = "IP")
    #description = tables.Column(verbose_name = "Descrição")
    #state = tables.Column(verbose_name = "Estado")
    partition_id = tables.Column(verbose_name = "Partition")
    class Meta(NetBoxTable.Meta):
        model = models.Node
        fields = [
            "name",
            "ipaddress_id",
            "state",
            "partition_id"
        ]

class PoolTable(NetBoxTable):
    name = tables.Column(linkify=True)
    '''pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:F5_bigip:pool", args=[A("pk")], verbose_name = "Nome pool")
    allownat = tables.Column(verbose_name = "Allow NAT")
    allowsnat = tables.Column(verbose_name = "Allow SNat")
    load_balancing_mode = tables.Column(verbose_name = "Load Balancing Mode")
    description = tables.Column(verbose_name = "Descrição")'''
    partition_id  = tables.Column(verbose_name = "Partition")

    class Meta(NetBoxTable.Meta):
        model = models.Pool
        fields = [
            "name",
            "load_balancing_mode",
            "partition_id",
        ]

class VirtualServerTable(NetBoxTable):
    name = tables.Column(linkify=True)
    '''pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:F5_bigip:virtualserver", args=[A("pk")],verbose_name = "Nome")
    mask = tables.Column(verbose_name = "Mascara")'''
    port = tables.Column(verbose_name = "Port")
    class Meta(NetBoxTable.Meta):
        model = models.VirtualServer
        fields = [
            "name",
            "VS_type",
            "port"
        ]

class VirtualAddressTable(NetBoxTable):
    #pk = columns.ToggleColumn()
    ipaddress_id = tables.Column(verbose_name = "IP")
    class Meta(NetBoxTable.Meta):
        model = models.VirtualAddress
        fields = [
            "ipaddress_id",
        ]

class PoolMemberTable(NetBoxTable):
    name = tables.Column(linkify=True)
    '''pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:F5_bigip:poolmember", args=[A("pk")],verbose_name = "Nome")'''
    node_id = tables.Column(verbose_name = "Node")
    #port = tables.Column("plugins:F5_bigip:port", args=[A("node_id.pk")], verbose_name = "Port")
    pool_id = tables.Column(verbose_name = "Pool")
    class Meta(NetBoxTable.Meta):
        model = models.PoolMember
        fields = [
            "name",
            "node_id",
            "port",
            "pool_id",
        ]

class Clusterf5Table(NetBoxTable):
    name = tables.Column(linkify=True)
    '''pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:F5_bigip:clusterf5", args=[A("pk")],verbose_name = "Nome")'''
    class Meta(NetBoxTable.Meta):
        model = models.Clusterf5
        fields = [
            "name",
        ]


class PartitionTable(NetBoxTable):
    name = tables.Column(linkify=True)
    '''pk = columns.ToggleColumn()
    name = tables.LinkColumn("plugins:F5_bigip:partition", args=[A("pk")],verbose_name = "Nome")'''
    clusterf5_id = tables.Column(verbose_name = "Cluster")

    class Meta(NetBoxTable.Meta):
        model = models.Partition
        fields = [
            "name",
            "clusterf5_id",
        ]

class IruleTable(NetBoxTable):
    name = tables.Column(linkify=True)
    #pk = columns.ToggleColumn()
    #name = tables.LinkColumn("plugins:F5_bigip:irule", args=[A("pk")],verbose_name = "Nome")
    partition_id = tables.LinkColumn(verbose_name = "Partition")
    #definition = tables.Column(verbose_name = "Definição")
    class Meta(NetBoxTable.Meta):
        model = models.Irule
        fields = [
            "name",
            "partition_id",
            "definition"
        ]

class Devicef5Table(NetBoxTable):
    name = tables.Column(linkify=True)
    #pk = columns.ToggleColumn()
    #name = tables.LinkColumn("plugins:F5_bigip:devicef5", args=[A("pk")],verbose_name = "Nome")
    device_id = tables.Column(verbose_name = "Device netbox")
    clusterf5_id = tables.Column(verbose_name = "Cluster")
    partition = tables.Column(verbose_name = "Cluster")
    class Meta(NetBoxTable.Meta):
        model = models.Devicef5
        fields = [
            "name",
            "clusterf5_id",
            "device_id"
        ]