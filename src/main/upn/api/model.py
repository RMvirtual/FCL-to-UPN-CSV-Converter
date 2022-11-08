from src.main.upn.api.client import UpnApiClient
from src.main.upn.api.parser import UpnApiParser


class UpnApi:
    def __init__(self):
        self._api = UpnApiClient()
        self._parser = UpnApiParser()

    def network_input(self):
        pass
