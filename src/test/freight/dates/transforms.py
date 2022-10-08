import unittest
from src.main.freight.dates import transforms


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_transform_ddmmyyyy_without_slashes(self):
        date = "23102022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_without_slashes(self):
        date = "231022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_with_slashes(self):
        date = "23\\10\\22"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyyyy_with_slashes(self):
        date = "23\\10\\2022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))



if __name__ == '__main__':
    unittest.main()
