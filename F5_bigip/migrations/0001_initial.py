# Generated by Django 5.0.5 on 2024-07-05 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),
        ('ipam', '0069_gfk_indexes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clusterf5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Cluster',
                'verbose_name_plural': 'Clusters',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Devicef5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('clusterf5_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.clusterf5')),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dcim.device')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Partition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('devicef5_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.devicef5')),
            ],
            options={
                'verbose_name': 'Partition',
                'verbose_name_plural': 'Partitions',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(default='Enabled', max_length=200)),
                ('ipaddress_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ipam.ipaddress')),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='F5_bigip.partition')),
            ],
            options={
                'verbose_name': 'Node',
                'verbose_name_plural': 'Nodes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Irule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('definition', models.TextField()),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.partition')),
            ],
            options={
                'verbose_name': 'Irule',
                'verbose_name_plural': 'Irules',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('allownat', models.CharField(blank=True, default='yes', max_length=200)),
                ('allowsnat', models.CharField(blank=True, default='yes', max_length=200)),
                ('load_balancing_mode', models.CharField(default='Round Robin', max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.partition')),
            ],
            options={
                'verbose_name': 'Pool',
                'verbose_name_plural': 'Pools',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PoolMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('port', models.CharField(max_length=65535)),
                ('state', models.CharField(default='Enabled', max_length=200)),
                ('node_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pools', to='F5_bigip.node')),
                ('pool_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='F5_bigip.pool')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VirtualAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('ipaddress_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ipam.ipaddress')),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.partition')),
            ],
            options={
                'verbose_name': 'Virtual Address',
                'verbose_name_plural': 'Virtual Addresses',
                'ordering': ['ipaddress_id'],
            },
        ),
        migrations.CreateModel(
            name='VirtualServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('port', models.CharField(max_length=65535)),
                ('VS_type', models.CharField(default='Standard', max_length=200)),
                ('irules', models.ManyToManyField(blank=True, related_name='virtual_servers', to='F5_bigip.irule')),
                ('partition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.partition')),
                ('pool_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='F5_bigip.pool')),
                ('virtualaddress_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='F5_bigip.virtualaddress')),
            ],
            options={
                'verbose_name': 'Virtual Server',
                'verbose_name_plural': 'Virtual Servers',
                'ordering': ['name'],
            },
        ),
    ]
