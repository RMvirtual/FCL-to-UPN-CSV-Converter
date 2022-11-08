import unittest
from src.main.upn.api.parser import UpnApiParser
from src.main.upn.api.structures import NetworkConsignmentStructure

class TestUpnApiParser(unittest.TestCase):
    def setUp(self):
        self._my_input = {

        }

        self._correct_output = {}

    def _set_up_network_consignment(self):
        self._my_input = {

        }

        self._correct_output = {}


    def _validate_network_consignment(
            self, consignment: NetworkConsignmentStructure):
        self.fail("DUMMY FAIL ON NETWORK CONSIGNMENT PARSER")

    def test_should_parse_network_consignment(self):
        self._set_up_network_consignment()
        parser = UpnApiParser()
        result = parser.network_consignment(self._my_input)
        self._validate_network_consignment(result)


if __name__ == '__main__':
    unittest.main()
