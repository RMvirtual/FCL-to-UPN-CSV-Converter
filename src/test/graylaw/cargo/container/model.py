import unittest
from src.test.graylaw.cargo.container import setup


class TestCargoModel(unittest.TestCase):
    def setUp(self):
        self._cargo = setup.two_entry_cargo()

    def test_should_total_weight(self) -> None:
        self.assertEqual(4200, self._cargo.total_weight)


if __name__ == "__main__":
    unittest.main()
