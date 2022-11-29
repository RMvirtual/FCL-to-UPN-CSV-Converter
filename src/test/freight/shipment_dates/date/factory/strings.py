import unittest
from src.main.freight.shipment_dates.date.factory.strings \
    import DatesAsStringsFactory


class TestDatesAsStringsFactory(unittest.TestCase):
    def setUp(self):
        self._factory = DatesAsStringsFactory()

    def test_should_create_dd_mm_yy(self) -> None:
        date = self._factory.dd_mm_yy("030691")

        self.assertEqual("03", date.day)
        self.assertEqual("06", date.month)
        self.assertEqual("91", date.year)

    def test_should_create_dd_mm_yyyy(self) -> None:
        date = self._factory.dd_mm_yyyy("03061991")

        self.assertEqual("03", date.day)
        self.assertEqual("06", date.month)
        self.assertEqual("1991", date.year)

    def test_should_create_dd_mm_yyyy_with_separators(self) -> None:
        date = self._factory.by_separator_characters("03/06/1991")

        self.assertEqual("03", date.day)
        self.assertEqual("06", date.month)
        self.assertEqual("1991", date.year)


if __name__ == '__main__':
    unittest.main()
