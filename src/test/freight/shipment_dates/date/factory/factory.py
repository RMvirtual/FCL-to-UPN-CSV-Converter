import unittest


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        self._correct_day = 23
        self._correct_month = 10
        self._correct_year = 2022

    def test_should_transform_ddmmyyyy_without_separators(self):
        self.fail()

    def test_should_transform_ddmmyyyy_with_separators(self):
        dates = ["23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022"]
        self.fail()

    def test_should_transform_ddmmyy_without_separators(self):
        date = "231022"
        self.fail()

    def test_should_transform_ddmmyy_with_separators(self):
        dates = ["23\\10\\22", "23-10-22", "23/10/22", "23.10.22"]
        self.fail()

    def test_should_transform_dd_mmm_yyyy_(self):
        dates = ["23-Oct-2022", "23-Oct-22"]
        self.fail()

    def test_should_transform_dd_mmmmm_yyyy_(self):
        dates = ["23-April-2022", "23-April-22"]
        self.fail()

    def test_should_transform_date_with_full_month_name(self):
        dates = ["23-September-2022", "23/September/22", " 23 September 2022"]
        self.fail()


if __name__ == '__main__':
    unittest.main()
