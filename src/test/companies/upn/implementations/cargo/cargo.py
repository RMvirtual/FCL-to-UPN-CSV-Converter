import unittest
from src.main.companies.upn.implementations.cargo.container import UPNCargo


class TestUPNCargo(unittest.TestCase):
    def setUp(self):
        self._cargo = UPNCargo()

    def test_should_add_pallet(self) -> None:
        self.fail("MOCK FAIL")


if __name__ == '__main__':
    unittest.main()
