import unittest
from src.test.companies.upn.imports.adaptors.freight.cargo.container import \
    setup

from src.main.companies.upn.system_import.adaptors.freight.cargo.containers \
    import UPNCargoAdaptor


class TestUPNCargoAdaptor(unittest.TestCase):
    def setUp(self):
        self._adaptor = UPNCargoAdaptor(setup.single_entry_upn_cargo())

    def test_should_adapt_total_weight(self) -> None:
        self.assertEqual(3000, self._adaptor.total_weight)

    def test_should_return_number_of_entries(self) -> None:
        self.assertEqual(1, len(self._adaptor))


if __name__ == '__main__':
    unittest.main()
