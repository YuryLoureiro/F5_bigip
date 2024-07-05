from netbox.plugins import PluginConfig
from .version import __version__



class F5bigipConfig(PluginConfig):
    name = "F5_bigip"
    base_url = "F5_bigip"
    verbose_name = "Plugin F5"
    description = "F5 BigIP Management for Netbox"
    version = __version__
    author = "Yury da Silva Loureiro"
    author_email = "yuryloureiro21@gmail.com"
    min_version = "4.0.0"
    max_version = "4.0.99"
    required_settings = []
    default_settings = {
        "supported_assets": [
            "dcim.device",
            "virtualization.virtualmachine",
            "tenancy.tenant",
            "dcim.site",
        ],
        "additional_assets": [],
        "proxies": {},
    }

config = F5bigipConfig  # noqa
