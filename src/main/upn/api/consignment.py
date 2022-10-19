import zeep
from src.main.file_system import api_files


class ConsignmentApiCall:
    def __init__(self):
        pass

    @staticmethod
    def get_network_input() -> None:
        upn_environment = api_files.upn_api()
        url = upn_environment["url"]
        client = zeep.Client(url)

        result = client.service.GetNetworkInput(
            "75", "18/10/2022",
            upn_environment["username"], upn_environment["password"]
        )

