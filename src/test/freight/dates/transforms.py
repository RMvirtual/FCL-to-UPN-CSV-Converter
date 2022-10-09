import unittest
from src.main.freight.dates import transforms


class TestDateTransforms(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_should_transform_ddmmyyyy_without_separators(self):
        date = "23102022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_without_separators(self):
        date = "231022"
        day, month, year = transforms.parse(date)

        self.assertTupleEqual((23, 10, 2022), (day, month, year))

    def test_should_transform_ddmmyy_with_separators(self):
        date_formats = [
            "23\\10\\22", "23-10-22", "23/10/22", "23.10.22"]

        for format in date_formats:
            day, month, year = transforms.parse(format)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year), msg=(
                    "Failed format:", format)
            )

    def test_should_transform_ddmmyyyy_with_separators(self):
        date_formats = [
            "23\\10\\2022", "23-10-2022", "23/10/2022", "23.10.2022"]

        for format in date_formats:
            day, month, year = transforms.parse(format)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year), msg=(
                    "Failed format:", format)
            )

    def test_should_transform_dd_mmm_yyyy_(self):
        date_formats = [
            "23-Oct-2022", "23-Oct-22"]

        for format in date_formats:
            day, month, year = transforms.parse(format)

            self.assertTupleEqual(
                (23, 10, 2022), (day, month, year), msg=(
                    "Failed format:", format)
            )

    def test_should_transform_dd_mmmmm_yyyy_(self):
        date_formats = [
            "23-April-2022", "23-April-22"]

        for format in date_formats:
            day, month, year = transforms.parse(format)

            self.assertTupleEqual(
                (23, 4, 2022), (day, month, year), msg=(
                    "Failed format:", format)
            )

    def test_should_transform_date_with_full_month_name(self):
        date_formats = [
            "23-September-2022", "23/September/22", " 23 September 2022"]

        for format in date_formats:
            day, month, year = transforms.parse(format)

            self.assertTupleEqual(
                (23, 9, 2022), (day, month, year), msg=(
                    "Failed format:", format)
            )


if __name__ == '__main__':
    unittest.main()
