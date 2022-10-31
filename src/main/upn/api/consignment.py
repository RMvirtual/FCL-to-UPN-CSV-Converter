import zeep
from src.main.file_system.file_contents import api_files


class ConsignmentApiCall:
    def __init__(self):
        self._environment = api_files.upn_api()
        self._client = zeep.Client(self._environment["url"])

    def get_network_input(self, date: str) -> list[dict]:
        """Returns a list of inbound consignments, collections
        requested and non-network input for a particular day.
        :param date: A string in yyyy-mm-dd format.
        """
        despatch_date = "2022-10-18T09:00:00"
        test_job = "GR221005418"
        barcode = "W213391123C"

        return self._client.service.GetNetworkInput(
            Depot=75,
            JobDate=date,
            Username=self._environment["username"],
            Password=self._environment["password"]
        )

    def get_post_code_restrictions(self, post_code: str) -> list[dict]:
        """Returns a list of restriction information for a particular
        postcode.

        :param post_code: A string representing the postcode area code
        (e.g. "AB10", "L24" or "EC2N").
        """
        return self._client.service.GetPostcodeRestrictions(
            Postcode=post_code,
            Username=self._environment["username"],
            Password=self._environment["password"]
        )
