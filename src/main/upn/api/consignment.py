import zeep
from src.main.file_system import api_files
import datetime


class ConsignmentApiCall:
    def __init__(self):
        pass

    @staticmethod
    def get_network_input() -> None:
        upn_environment = api_files.upn_api()
        url = upn_environment["url"]
        client = zeep.Client(url)

        depot = 75
        despatch_date = "2022-10-18T09:00:00"
        test_job = "GR221005418"
        barcode = "W213391123C"

        base_64 = client.get_type(
            "xsd:ArrayOfbase64Binary")

        print(base_64)

        """
        result = client.service.PalletLabels(
            barcode, depot,
            upn_environment["username"], upn_environment["password"]
        )

        print(result)
        """