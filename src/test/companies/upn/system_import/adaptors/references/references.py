import unittest
from src.main.companies.upn.system_import.adaptors.references.adaptor \
    import UPNReferencesAdaptor

from src.main.companies.upn.api.implementation_1.api.references.references \
    import UPNReferences


class TestUPNReferencesAdaptor(unittest.TestCase):
    def setUp(self):
        self._references = UPNReferences()
        self._references.barcode = "W123456789C"
        self._references.consignment_no = "GR221105306"
        self._references.customer_reference = "PHILLIP"

    def test_should_adapt_upn_reference(self) -> None:
        adaptor = UPNReferencesAdaptor(self._references)
        self.assertEqual("GR221105306", str(adaptor.consignment))
        self.assertListEqual(["PHILLIP"], adaptor.shipper)
        self.assertListEqual([], adaptor.consignee)


if __name__ == '__main__':
    unittest.main()
