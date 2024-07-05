from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label="F5 BigIP",
    icon_class="mdi mdi-spider",
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
            ),
        ),
    ),
)