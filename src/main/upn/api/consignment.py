import requests
from src.main.file_system import api_files


class ConsignmentApiCall:
    def __init__(self):
        pass

    @staticmethod
    def get_network_input() -> None:
        upn_environment = api_files.upn_api()

        response = requests.get(
            url=upn_environment["url"],
            params=(
                "Depot=" + upn_environment["depot"]
                + "&JobDate=" + "17/10/2022"
                + "&Username=" + upn_environment["username"]
                + "&Password=" + upn_environment["password"]
            )
        )

        print(response.text)

