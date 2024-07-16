from django.db.models import Q
from utilities.choices import ChoiceSet

class PoolBalancingChoices(ChoiceSet):
    LOADBALANCING_1 = "Round Robin"
    LOADBALANCING_2 = "Ratio (member)"
    LOADBALANCING_3 = "Least Connections (member)"
    LOADBALANCING_4 = "Observed (member)"
    LOADBALANCING_5 = "Predictive (member)"
    LOADBALANCING_6 = "Ratio (node)"
    LOADBALANCING_7 = "Least Connections (node)"
    LOADBALANCING_8 = "Fastest (node)"
    LOADBALANCING_9 = "Observed (node)"
    LOADBALANCING_10 = "Predictive (node)"
    LOADBALANCING_11 = "Dynamic Ratio (node)"
    LOADBALANCING_12 = "Fastest (application)"
    LOADBALANCING_13 = "Least Sessions"
    LOADBALANCING_14 = "Dynamic Ratio (member)"
    LOADBALANCING_15 = "Weighted Least Connections (member)"
    LOADBALANCING_16 = "Weighted Least Connections (node)"
    LOADBALANCING_17 = "Ratio (session)"
    LOADBALANCING_18 = "Ratio Least Connections (member)"
    LOADBALANCING_19 = "Ratio Least Connections (node)"


    CHOICES = (
        (LOADBALANCING_1, "Round Robin"),
        (LOADBALANCING_2, "Ratio (member)"),
        (LOADBALANCING_3, "Least Connections (member)"),
        (LOADBALANCING_4, "Observed (member)"),
        (LOADBALANCING_5, "Predictive (member)"),
        (LOADBALANCING_6, "Ratio (node)"),
        (LOADBALANCING_7, "Least Connections (node)"),
        (LOADBALANCING_8, "Fastest (node)"),
        (LOADBALANCING_9, "Observed (node)"),
        (LOADBALANCING_10, "Predictive (node)"),
        (LOADBALANCING_11, "Dynamic Ratio (node)"),
        (LOADBALANCING_12, "Fastest (application)"),
        (LOADBALANCING_13, "Least Sessions"),
        (LOADBALANCING_14, "Dynamic Ratio (member)"),
        (LOADBALANCING_15, "Weighted Least Connections (member)"),
        (LOADBALANCING_16, "Weighted Least Connections (node)"),
        (LOADBALANCING_17, "Ratio (session)"),
        (LOADBALANCING_18, "Ratio Least Connections (member)"),
        (LOADBALANCING_19, "Ratio Least Connections (node)"),
    )

class StateChoices(ChoiceSet):
    STATE_ENABLED = "Enabled"
    STATE_DISABLED = "Disabled"

    CHOICES = (
        (STATE_ENABLED, 'Enabled'),
        (STATE_DISABLED, 'Disabled'),
    )

class AStateChoices(ChoiceSet):
    STATE_ENABLED = "Enabled"
    STATE_DISABLED = "Disabled"
    STATE_FO = "Forced Offline"

    CHOICES = (
        (STATE_ENABLED, 'Enabled'),
        (STATE_DISABLED, 'Disabled'),
        (STATE_FO, 'Forced Offline'),
    )

class PoolAllowChoices(ChoiceSet):
    CHOICE_YES = 'yes'
    CHOICE_NO = 'no'

    CHOICES = (
        (CHOICE_YES, 'Yes', 'blue'),
        (CHOICE_NO, 'No', 'red'),
    )

class VirtServerChoices(ChoiceSet):
    VIRTUALSERVER_1 = "Standard"
    VIRTUALSERVER_2 = "Forwarding (Layer 2)"
    VIRTUALSERVER_3 = "Forwarding (IP)"
    VIRTUALSERVER_4 = "Performance (HTTP)"
    VIRTUALSERVER_5 = "Performance (Layer 4)"
    VIRTUALSERVER_6 = "Stateless"
    VIRTUALSERVER_7 = "Reject"
    VIRTUALSERVER_8 = "DHCP"
    VIRTUALSERVER_9 = "Internal"
    VIRTUALSERVER_10 = "Message Routing"

    CHOICES = (
        (VIRTUALSERVER_1, "Standard"),
        (VIRTUALSERVER_2, "Forwarding (Layer 2)"),
        (VIRTUALSERVER_3, "Forwarding (IP)"),
        (VIRTUALSERVER_4, "Performance (HTTP)"),
        (VIRTUALSERVER_5, "Performance (Layer 4)"),
        (VIRTUALSERVER_6, "Stateless"),
        (VIRTUALSERVER_7, "Reject"),
        (VIRTUALSERVER_8, "DHCP"),
        (VIRTUALSERVER_9, "Internal"),
        (VIRTUALSERVER_10, "Message Routing"),
    )