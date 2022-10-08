import unittest
from src.main.freight.dates import transforms


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_transform_dd_mm_yyyy_without_slashes(self):
        date = "23102022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))


if __name__ == '__main__':
    unittest.main()
