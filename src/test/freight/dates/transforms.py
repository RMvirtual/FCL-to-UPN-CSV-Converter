import unittest
from src.main.freight.dates import transforms


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_transform_ddmmyyyy_without_separators(self):
        self._assert_date_transform_produces((23, 10, 2022), "23102022")

    def test_should_transform_ddmmyy_without_separators(self):
        self._assert_date_transform_produces((23, 10, 2022), "231022")

    def test_should_transform_ddmmyy_with_separators(self):
        self._assert_date_transforms_produce(
            (23, 10, 2022), ["23\\10\\22", "23-10-22", "23/10/22", "23.10.22"])

    def test_should_transform_ddmmyyyy_with_separators(self):
        self._assert_date_transforms_produce(
            (23, 10, 2022),
            ["23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022"]
        )

    def test_should_transform_dd_mmm_yyyy_(self):
        self._assert_date_transforms_produce(
            (23, 10, 2022), ["23-Oct-2022", "23-Oct-22"])

    def test_should_transform_dd_mmmmm_yyyy_(self):
        self._assert_date_transforms_produce(
            (23, 4, 2022), ["23-April-2022", "23-April-22"])

    def test_should_transform_date_with_full_month_name(self):
        self._assert_date_transforms_produce(
            (23, 9, 2022),
            ["23-September-2022", "23/September/22", " 23 September 2022"]
        )

    def _assert_date_transforms_produce(
            self, correct_dd_mm_yyyy: tuple[int, int, int],
            dates: list[str]
    ) -> None:
        for date in dates:
            self._assert_date_transform_produces(correct_dd_mm_yyyy, date)

    def _assert_date_transform_produces(
            self, correct_dd_mm_yyyy: tuple[int, int, int], date: str) -> None:
        fail_message = "Failed date: " + date
        dd_mm_yyyy = transforms.parse(date)

        self.assertTupleEqual(correct_dd_mm_yyyy, dd_mm_yyyy, msg=fail_message)


if __name__ == '__main__':
    unittest.main()
