# Generated by Django 5.0.5 on 2024-07-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('F5_bigip', '0005_remove_node_state_virtualserver_source_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='state',
            field=models.CharField(default='Enabled', max_length=200),
        ),
    ]
