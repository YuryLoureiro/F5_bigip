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
                    link="plugins:F5_bigip:node",
                    link_text="Node",
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
                    link="plugins:F5_bigip:pool",
                    link_text="Pool",
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
                    link="plugins:F5_bigip:virtualserver",
                    link_text="Virtual Server",
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
                    link="plugins:F5_bigip:virtualaddress",
                    link_text="Virtual Address",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:virtualaddress_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:poolmember",
                    link_text="Pool Member",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:poolmember_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:clusterf5",
                    link_text="Cluster",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:clusterf5_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:partition",
                    link_text="Partition",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:partition_add",
                            "Add",
                            "mdi mdi-plus-thick",
                            permissions=["F5_bigip.admin_full"],
                        ),
                    ),
                ),
                PluginMenuItem(
                    permissions=["F5_bigip.admin_full"],
                    link="plugins:F5_bigip:devicef5",
                    link_text="Device",
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
                    link="plugins:F5_bigip:irule",
                    link_text="iRule",
                    buttons=(
                        PluginMenuButton(
                            "plugins:F5_bigip:irule_add",
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