import unittest


class TestDateFactory(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_day = 23
        self._correct_month = 10
        self._correct_year = 2022

    def test_should_create_from_ddmmyyyy_without_separators(self) -> None:
        self.fail()

    def test_should_create_from_ddmmyyyy_with_separators(self) -> None:
        dates = ("23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022")
        self.fail()

    def test_should_create_from_ddmmyy_without_separators(self) -> None:
        date = "231022"
        self.fail()

    def test_should_create_from_ddmmyy_with_separators(self) -> None:
        dates = ("23\\10\\22", "23-10-22", "23/10/22", "23.10.22")
        self.fail()

    def test_should_create_from_dd_mmm_yyyy_(self) -> None:
        dates = ("23-Oct-2022", "23-Oct-22")
        self.fail()

    def test_should_create_from_dd_mmmmm_yyyy_(self) -> None:
        dates = ("23-April-2022", "23-April-22")
        self.fail()

    def test_should_create_from_date_with_full_month_name(self) -> None:
        dates = ("23-September-2022", "23/September/22", " 23 September 2022")
        self.fail()


if __name__ == '__main__':
    unittest.main()
