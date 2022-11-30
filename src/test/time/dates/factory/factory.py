import unittest
from src.main.time.dates import factory


class TestDateFactory(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_day = 23
        self._correct_month = 10
        self._correct_year = 2022

    def test_should_create_from_numeric_date(self) -> None:
        dates = ["231022", "23102022"]
        self.fail()

    def test_should_create_from_numeric_delimited_date(self) -> None:
        dates = [
            "23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022",
            "23\\10\\22", "23-10-22", "23/10/22", "23.10.22"
        ]

        self.fail()

    def test_should_create_from_alphanumeric_date(self) -> None:
        dates = [
            "23-Oct-2022", "23-Oct-22", "23-April-2022", "23-April-22",
            "23-September-2022", "23/September/22", " 23 September 2022"
        ]


if __name__ == '__main__':
    unittest.main()
