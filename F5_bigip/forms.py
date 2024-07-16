
from .models import Clusterf5, Devicef5, Irule, Node, Partition, Pool, PoolMember, VirtualAddress, VirtualServer
from .choices import *
from django.forms import formset_factory

from django import forms
from django.contrib.contenttypes.models import ContentType

from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelFilterSetForm,
    NetBoxModelBulkEditForm,
    NetBoxModelImportForm,
)
from ipam.models import IPAddress
from dcim.models import Device, DeviceType
from utilities.forms.fields import (
    DynamicModelMultipleChoiceField,
    SlugField,
    DynamicModelChoiceField,
    CSVModelMultipleChoiceField,
    CSVModelChoiceField,
    CSVContentTypeField,
)
from utilities.forms.rendering import FieldSet


class NodeFilterForm(NetBoxModelFilterSetForm):
    model = Node
    q = forms.CharField(
        required=False,
        label='Search'
    )

class NodeBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    status = forms.ChoiceField(
        required=False,
        choices=StateChoices,
    )

    model = Node
    nullable_fields = [
       'description',
    ]
    
class PoolFilterForm(NetBoxModelFilterSetForm):
    model = Pool
    q = forms.CharField(
        required=False,
        label='Search'
    )
    state = forms.MultipleChoiceField(
        choices=PoolAllowChoices,
        required=False,
    )

class PoolBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Pool.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = Pool
    nullable_fields = [
       'description',
    ]

class PoolMemberFilterForm(NetBoxModelFilterSetForm):
    model = PoolMember
    q = forms.CharField(
        required=False,
        label='Search'
    )

'''class PoolMemberBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=PoolMember.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = PoolMember
    nullable_fields = [
       'description',
    ]'''
class PoolMemberEditForm(NetBoxModelForm):
    class Meta:
        model = PoolMember
        fields = ['name', 'node_id', 'port', 'state', 'description']

    name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    node_id = forms.ModelChoiceField(
        queryset=PoolMember.objects.all(),
        required=False,
        label='Node name',
        widget=forms.Select(attrs={'readonly': 'readonly', 'disabled': 'disabled'})
    )
    port = forms.CharField(
        max_length=65535,
        required=False,
        label='Service Port',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    state = forms.ChoiceField(
        choices=AStateChoices,
        required=False
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )


class PoolMemberBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=PoolMember.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    state = forms.ChoiceField(
        choices=AStateChoices,
        required=False
    )

    name = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    node_id = forms.ModelChoiceField(
        queryset=PoolMember.objects.all(),
        required=False,
        widget=forms.Select(attrs={'readonly': 'readonly', 'disabled': 'disabled'})
    )
    port = forms.CharField(
        max_length=65535,
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    class Meta:
        model = PoolMember
        fields = ['description', 'state', 'name', 'node_id', 'port']
        nullable_fields = ['description']

class VirtualServerFilterForm(NetBoxModelFilterSetForm):
    model = VirtualServer
    q = forms.CharField(
        required=False,
        label='Search'
    )

class VirtualServerBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=VirtualServer.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = VirtualServer
    nullable_fields = [
       'description',
    ]


class VirtualAddressFilterForm(NetBoxModelFilterSetForm):
    model = VirtualAddress
    q = forms.CharField(
        required=False,
        label='Search'
    )

class VirtualAddressBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=VirtualAddress.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = VirtualAddress
    nullable_fields = [
       'description',
    ]

class Clusterf5FilterForm(NetBoxModelFilterSetForm):
    model = Clusterf5
    q = forms.CharField(
        required=False,
        label='Search'
    )

class Clusterf5BulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Clusterf5.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = Clusterf5
    nullable_fields = [
       'description',
    ]

class PartitionFilterForm(NetBoxModelFilterSetForm):
    model = Partition
    q = forms.CharField(
        required=False,
        label='Search'
    )

class PartitionBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Partition.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = Partition
    nullable_fields = [
       'description',
    ]

class IruleFilterForm(NetBoxModelFilterSetForm):
    model = Irule
    q = forms.CharField(
        required=False,
        label='Search'
    )

class IruleBulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Irule.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = Irule
    nullable_fields = [
       'description',
    ]

class Devicef5FilterForm(NetBoxModelFilterSetForm):
    model = Devicef5
    q = forms.CharField(
        required=False,
        label='Search'
    )
    #tag = TagFilterField(model)

class Devicef5BulkEditForm(NetBoxModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=Devicef5.objects.all(),
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )

    model = Devicef5
    nullable_fields = [
       'description',
    ]

class NodeForm(NetBoxModelForm):
    name = forms.CharField(
        required=True,
        label='Nome do Node'
    )
    ipaddress_id = forms.ModelChoiceField(queryset = IPAddress.objects.all() ,label='IP Address')
    partition_id = forms.ModelChoiceField(queryset = Partition.objects.all() ,label='Partition')
    class Meta:
        model = Node
        fields = [
            "name",
            "ipaddress_id",
            "description",
            "partition_id"
        ]

'''class PoolForm(NetBoxModelForm):
    name = forms.CharField(
        required=True,
        label='Nome da pool'
    )
    partition_id = forms.ModelChoiceField(queryset = Partition.objects.all() ,label='Partition')
    new_members = forms.ModelChoiceField(
        queryset = Node.objects.all(), 
        label='New Members',
        required=True,
    )
    class Meta:
        model = Pool
        fields = [
            "name",
            "allownat",
            "allowsnat",
            "load_balancing_mode",
            "description",
            "partition_id",
        ]
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            pool_members_names = self.cleaned_data['new_members'].split(',')
            for name in pool_members_names:
                if name.strip():  # Avoid creating empty devices
                    PoolMember.objects.create(name=name.strip(), clusterf5_id=instance)
        return instance'''
'''class PoolForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='Nome da pool',
        widget=forms.TextInput(attrs={'id': 'id_name'})
    )
    partition_id = forms.ModelChoiceField(
        queryset=Partition.objects.all(),
        label='Partition',
        widget=forms.Select(attrs={'id': 'id_partition_id'})
    )
    new_members = forms.ModelMultipleChoiceField(
        queryset=Node.objects.none(),
        label='New Members',
        required=True,
        widget=forms.CheckboxSelectMultiple(attrs={'id': 'id_new_members'})
    )
    ports = forms.CharField(
        required=True,
        label='Ports (comma-separated, matching order of nodes selected)',
        widget=forms.TextInput(attrs={'id': 'id_ports'})
    )

    class Meta:
        model = Pool
        fields = [
            "name",
            "allownat",
            "allowsnat",
            "load_balancing_mode",
            "description",
            "partition_id",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'partition_id' in self.data:
            try:
                partition_id = int(self.data.get('partition_id'))
                self.fields['new_members'].queryset = Node.objects.filter(partition_id=partition_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['new_members'].queryset = self.instance.partition_id.node_set

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            selected_nodes = self.cleaned_data['new_members']
            ports = self.cleaned_data['ports'].split(',')
            for node, port in zip(selected_nodes, ports):
                PoolMember.objects.create(
                    name=node.name,
                    node_id=node,
                    port=port.strip(),
                    pool_id=instance,
                    state=PoolMember.STATE_ENABLED
                )
        return instance'''

class PoolForm(NetBoxModelForm):
    name = forms.CharField(
        required=True,
        label='Nome da pool'
    )
    partition_id = forms.ModelChoiceField(queryset=Partition.objects.all(), label='Partition')
    new_members = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        label='New Members',
        required=True,
    )
    ports = forms.CharField(
        required=True,
        label='Ports (comma-separated, one for each member)'
    )

    class Meta:
        model = Pool
        fields = [
            "name",
            "allownat",
            "allowsnat",
            "load_balancing_mode",
            "description",
            "partition_id",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            selected_nodes = self.cleaned_data['new_members']
            ports = self.cleaned_data['ports'].split(',')
            for node, port in zip(selected_nodes, ports):
                PoolMember.objects.create(
                    name=node.name,
                    node_id=node,
                    port=port.strip(),
                    pool_id=instance,
                    state=StateChoices.STATE_ENABLED  # Default state
                )
        return instance

class VirtualServerForm(NetBoxModelForm):
    name = forms.CharField(label='Name')
    description = forms.CharField(
        required=False,
        label="Description",
    )
    port = forms.CharField(
        label="Port",
    )
    state = forms.ChoiceField(
        choices=StateChoices,
        required=True,
    )
    VS_type = forms.ChoiceField(
        choices=VirtServerChoices,
        label="Type",
        required=True,
    )
    source_address = forms.CharField(
        required=True,
        label="Source Address",
    )
    partition_id = forms.ModelChoiceField(
        queryset=Partition.objects.all(),
        required=True,
        label="Partition",
    )
    irules = forms.ModelMultipleChoiceField(
        queryset=Irule.objects.all(),
        label='iRules',
        required=False,
    )

    class Meta:
        model = VirtualServer
        fields = [
            "name",
            "description",
            "VS_type",
            "source_address",
            "port",
            "state",
            "partition_id",
            "irules"
        ]

    def save(self, commit=True):
        virtual_server = super().save(commit=False)
        if commit:
            virtual_server.save()
        self.save_m2m()
        return virtual_server


class VirtualAddressForm(NetBoxModelForm):
    ipaddress_id = forms.ModelChoiceField(queryset = IPAddress.objects.all() ,label='IP Address')
    class Meta:
        model = VirtualAddress
        fields = [
            "ipaddress_id",
        ]

class Clusterf5Form(forms.ModelForm):
    name = forms.CharField(label='Name')
    class Meta:
        model = Clusterf5
        fields = [
            "name",
        ]

class PartitionForm(NetBoxModelForm):
    name = forms.CharField(label = 'Name')
    clusterf5_id = forms.ModelChoiceField(queryset = Clusterf5.objects.all() ,label='Cluster', required=True)
    class Meta:
        model = Partition
        fields = [
            "name",
        ]

class IruleForm(NetBoxModelForm):
    name = forms.CharField(label = 'Name')
    partition_id = forms.ModelChoiceField(
        queryset=Partition.objects.all(),
        required=True,
        label="Partition",
    )
    class Meta:
        model = Irule
        fields = [
            "name",
            "partition_id",
            "definition",
        ]

class Devicef5Form(NetBoxModelForm):
    name = forms.CharField(label='Name')
    device_id = forms.ModelChoiceField(queryset=Device.objects.all(), label='Device', required=True)
    clusterf5_id = forms.ModelChoiceField(queryset=Clusterf5.objects.all(), label='Cluster', required=False)
    partitions = forms.CharField(
        label='Partitions', 
        required=False, 
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='Enter partition names separated by commas'
    )

    class Meta:
        model = Devicef5
        fields = [
            "name",
            "device_id",
            "clusterf5_id",
            "partitions",  # Add partitions field
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            # Clear existing partitions
            Partition.objects.filter(devicef5_id=instance).delete()
            # Add new partitions
            partition_names = self.cleaned_data['partitions'].split(',')
            for name in partition_names:
                if name.strip():  # Avoid creating empty partitions
                    Partition.objects.create(name=name.strip(), devicef5_id=instance)
        return instance

""" class SettingsForm(NetBoxModelForm):
    class Meta:
        model = Settings
        fields = [
            "hostname",
            "username",
            "password",
            "version",
            "verify",
            "status",
        ]
        widgets = {
            "status": StaticSelect(
                choices=(
                    ("True", "Yes"),
                    ("False", "No"),
                )
            ),
            "verify": StaticSelect(
                choices=(
                    (True, "Yes"),
                    (False, "No"),
                )
            ),
        } """