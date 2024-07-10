from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label="F5 BigIP",
    icon_class="mdi mdi-flag-checkered",
    groups=(
        (
            "BigIP",
            (
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:virtualserver",
                    link_text="Virtual Servers",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:virtualserver_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:irule",
                    link_text="iRules",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:irule_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:pool",
                    link_text="Pools",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:pool_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:node",
                    link_text="Nodes",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:node_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:devicef5",
                    link_text="Devices",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:devicef5_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:clusterf5",
                    link_text="Clusters",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:clusterf5_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
            ),
        ),
    ),
)