import zeep
from src.main.file_system.file_contents import api_files


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

        # zeep.xsd.String
        # integer_type.accept(75)
        # print(integer_type)

        result = client.service.GetPostcodeRestrictions(
            Postcode="AB10",
            Username=upn_environment["username"],
            Password=upn_environment["password"]
        )

        print(result)
