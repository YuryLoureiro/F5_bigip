from netbox.filtersets import NetBoxModelFilterSet
from django.db.models import Q
import django_filters

from .models import Devicef5, Irule, Node, Partition, Pool, PoolMember, Clusterf5, VirtualServer, VirtualAddress


class NodeFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = Node
        fields = ['name', 'ipaddress_id', 'description', 'state', 'partition_id']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

    def state(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                Q(state__icontains=value)
        )
        return queryset.filter(qs_filter)

class PoolFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Pool
        fields = ['name', 'allownat', 'allowsnat', 'load_balancing_mode', 'description', 'partition_id']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class PoolMemberFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = PoolMember
        fields = ['name', 'node_id', 'port', 'pool_id', 'state']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class VirtualServerFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = VirtualServer
        fields = ['name', 'description', 'port', 'pool_id', 'partition_id', 'irules']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class VirtualAddressFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = VirtualAddress
        fields = ['name', 'ipaddress_id']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(ipaddress_id__icontains=value)
        )
        return queryset.filter(qs_filter)

class Clusterf5FilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Clusterf5
        fields = ['name']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class PartitionFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Partition
        fields = ['name']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class IruleFilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Irule
        fields = ['name','partition_id','definition']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)

class Devicef5FilterSet(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    #tag = TagFilter()

    class Meta:
        model = Devicef5
        fields = ['name','device_id','clusterf5_id']

    def search(self, queryset, name, value):
        """Perform the filtered search."""
        if not value.strip():
            return queryset
        qs_filter = (
                #Q(id__icontains=value)
                Q(name__icontains=value)
        )
        return queryset.filter(qs_filter)