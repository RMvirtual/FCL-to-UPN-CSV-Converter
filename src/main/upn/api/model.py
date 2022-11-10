from src.main.upn.api.client.soap_api import UpnApiClient
from src.main.upn.api.parser.parser import UpnApiParser


class UpnApi:
    def __init__(self):
        self._api = UpnApiClient()
        self._parser = UpnApiParser()

    def network_input(self):
        pass
