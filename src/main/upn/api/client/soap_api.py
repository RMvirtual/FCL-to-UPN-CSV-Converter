import zeep
from src.main.file_system.upn.api import configuration


class UPNAPIClient:
    def __init__(self):
        self._environment = configuration.upn_api()
        self._client = zeep.Client(self._environment["url"])

    def network_input(self, date: str) -> list[dict]:
        """Returns a list of inbound adaptors, collections
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

    def network_deliveries(self, date: str) -> list[dict]:
        """Returns a list of deliveries completed on behalf of the
        network for a particular day (does not include collections
        received).
        :param date: A string in yyyy-mm-dd format.
        """
        return self._client.service.GetNetworkDeliveries(
            Depot=75,
            JobDate=date,
            Username=self._environment["username"],
            Password=self._environment["password"]
        )

    def network_delivery_by_con_no(self, con_no: str):
        """Only seems to work with the depot number api parameter
        being the actual depot of delivery (e.g. 75 for local dels,
        depot 9 for NE deliveries).
        """
        array_of_string = self._client.get_type("ns3:ArrayOfstring")
        value_to_pass = array_of_string([con_no])

        return self._client.service.GetNetworkDeliveryByConNo(
            Depot=75,
            ConNo=value_to_pass,
            Username=self._environment["username"],
            Password=self._environment["password"]
        )

    def post_code_restrictions(self, post_code: str) -> list[dict]:
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
