import zeep
from src.main.file_system.file_contents import api_files


class ConsignmentApiCall:
    def __init__(self):
        pass

    @staticmethod
    def get_network_input(date: str) -> list[dict]:
        """Returns a list of inbound consignments, collections
        requested and non-network input for a particular day.
        :param date: A string in yyyy-mm-dd format.
        """
        upn_environment = api_files.upn_api()
        client = zeep.Client(upn_environment["url"])

        despatch_date = "2022-10-18T09:00:00"
        test_job = "GR221005418"
        barcode = "W213391123C"

        return client.service.GetNetworkInput(
            Depot=75,
            JobDate=date,
            Username=upn_environment["username"],
            Password=upn_environment["password"]
        )

    @staticmethod
    def get_post_code_restrictions(post_code: str) -> list[dict]:
        """Returns a list of restriction information for a particular
        postcode.
        """
        upn_environment = api_files.upn_api()
        client = zeep.Client(upn_environment["url"])

        return client.service.GetPostcodeRestrictions(
            Postcode=post_code,
            Username=upn_environment["username"],
            Password=upn_environment["password"]
        )
