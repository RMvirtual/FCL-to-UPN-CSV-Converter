import unittest
from src.main.upn.consignment.cargo.package.pallet.abstract import (
    AbstractUPNPallet, UPNPalletFields)


class TestUPNAbstractPallet(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_instantiate_abstract_upn_pallet(self) -> None:
        fields = UPNPalletFields()
        fields.type = "FULL"
        fields.size = "N"
        fields.size_constraints = ["N", "O", "2", "3"]
        fields.type_constraints = ["FULL", "HALF"]

        pallet = AbstractUPNPallet(fields)
        self.assertEqual("FULL", pallet.type)
        self.assertEqual("N", pallet.size)


if __name__ == '__main__':
    unittest.main()
