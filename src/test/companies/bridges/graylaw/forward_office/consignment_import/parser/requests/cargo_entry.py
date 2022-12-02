import unittest
from src.main.companies.bridges.graylaw.graylaw.forward_office\
    .consignment_import.parser.requests.types \
    import CargoEntryParseRequest


class TestCargoEntryParseRequest(unittest.TestCase):
    def setUp(self):
        self._request = CargoEntryParseRequest()
        self._request.quantity = 0
        self._request.package_type = None
        self._request.goods_description = ""
        self._request.weight = 0

    def test_should_show_as_empty_request(self):
        self.assertTrue(self._request.is_empty())


if __name__ == '__main__':
    unittest.main()
