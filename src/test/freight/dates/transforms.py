import unittest
from src.main.freight.dates import transforms


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_transform_ddmmyyyy_without_separators(self):
        day, month, year = transforms.parse("23102022")

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_without_separators(self):
        day, month, year = transforms.parse("231022")

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_with_separators(self):
        dates = ["23\\10\\22", "23-10-22", "23/10/22", "23.10.22"]

        for date in dates:
            day, month, year = transforms.parse(date)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year),
                msg=("Failed format:", date)
            )

    def test_should_transform_ddmmyyyy_with_separators(self):
        dates = ["23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022"]

        for date in dates:
            day, month, year = transforms.parse(date)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year),
                msg=("Failed format:", date)
            )

    def test_should_transform_dd_mmm_yyyy_(self):
        dates = ["23-Oct-2022", "23-Oct-22"]

        for date in dates:
            day, month, year = transforms.parse(date)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year),
                msg=("Failed format:", date)
            )

    def test_should_transform_dd_mmmmm_yyyy_(self):
        dates = ["23-April-2022", "23-April-22"]

        for date in dates:
            day, month, year = transforms.parse(date)

            self.assertTupleEqual(
                (23, 4, 2022), (day, month, year), msg=("Failed format:", date)
            )

    def test_should_transform_date_with_full_month_name(self):
        dates = ["23-September-2022", "23/September/22", " 23 September 2022"]

        for date in dates:
            self._assert_date_transform_produces((23, 9, 2022), date)

    def _assert_date_transform_produces(
            self, correct_dd_mm_yyyy: tuple[int, int, int], date: str) -> None:
        self.assertTupleEqual(
            correct_dd_mm_yyyy, transforms.parse(date),
            msg="Failed date:" + date
        )


if __name__ == '__main__':
    unittest.main()
