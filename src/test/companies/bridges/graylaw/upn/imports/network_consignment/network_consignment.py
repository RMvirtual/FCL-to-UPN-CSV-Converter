import unittest
from src.main.companies.bridges.graylaw.upn.imports.network_consignment\
    .adaptor import NetworkConsignmentAdaptor


from src.test.companies.bridges.graylaw.upn.imports.network_consignment\
    .setup import \
    graylaw_setup, upn_setup


class TestUPNNetworkConsignmentAdaptor(unittest.TestCase):
    def setUp(self):
        self._network_consignment = upn_setup.dummy_network_consignment()
        self._correct_graylaw_consignment = graylaw_setup.dummy_consignment()
        self._adaptor = NetworkConsignmentAdaptor(self._network_consignment)

    def test_should_adapt_consignment_reference(self) -> None:
        references = self._adaptor.references

        self.assertEqual("GR221004388", str(references.consignment))


if __name__ == '__main__':
    unittest.main()
