# Generated by Django 5.0.5 on 2024-07-06 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('F5_bigip', '0002_node_created_node_custom_field_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='created',
        ),
        migrations.RemoveField(
            model_name='node',
            name='custom_field_data',
        ),
        migrations.RemoveField(
            model_name='node',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='node',
            name='tags',
        ),
    ]