import unittest
from src.test.upn.consignment.adaptors.cargo import setup
from src.main.upn.consignment.adaptors.cargo import UPNCargoAdaptor


class TestUPNCargoAdaptor(unittest.TestCase):
    def setUp(self):
        self._adaptor = UPNCargoAdaptor(setup.single_entry_upn_cargo())

    def test_should_adapt_upn_cargo(self) -> None:
        self.fail("MOCK FAIL")


if __name__ == '__main__':
    unittest.main()
