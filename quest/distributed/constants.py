"""
Constains all the constant identifiers used to talk about Distributed Objects across the system.
"""

import enum

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class NetworkGlobalObjectIds(enum.IntEnum):
    """
    """

    DOG_LOGIN_MANAGER = 1000

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class NetworkChannels(enum.IntEnum):
    """
    """

    UBERDOG_CHANNEL = 300000
    AI_CHANNEL = 300001
    STATE_SERVER_CHANNEL = 402000

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#