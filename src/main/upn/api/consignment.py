import zeep
from src.main.file_system.file_contents import api_files


class ConsignmentApiCall:
    def __init__(self):
        pass

    @staticmethod
    def get_network_input():
        upn_environment = api_files.upn_api()
        client = zeep.Client(upn_environment["url"])

        depot = 75
        despatch_date = "2022-10-18T09:00:00"
        test_job = "GR221005418"
        barcode = "W213391123C"

        # zeep.xsd.String
        # integer_type.accept(75)
        # print(integer_type)

        return client.service.GetNetworkInput(
            Depot=75,
            JobDate="2022-10-18",
            Username=upn_environment["username"],
            Password=upn_environment["password"]
        )

    @staticmethod
    def get_post_code_restrictions(post_code: str):
        upn_environment = api_files.upn_api()
        client = zeep.Client(upn_environment["url"])

        return client.service.GetPostcodeRestrictions(
            Postcode=post_code,
            Username=upn_environment["username"],
            Password=upn_environment["password"]
        )
