"""
Listing Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class NexxeraConfig(AppConfig):
    name = 'nexxera_api'

    def ready(self):
        import nexxera_api.signals
