import unittest
from src.main.graylaw.cargo.packages.oversize.options import OversizeOption


class TestOversizeOption(unittest.TestCase):
    def setUp(self):
        pass

    def test_should_show_oversize_options_as_equal(self) -> None:
        self.assertEqual(self._normal_oversize(), self._normal_oversize())

    def test_should_show_oversize_options_as_inequal(self) -> None:
        self.assertNotEqual(self._normal_oversize(), self._double_oversize())

    @staticmethod
    def _normal_oversize() -> OversizeOption:
        return OversizeOption(name="normal", multiplier=1.0)

    @staticmethod
    def _double_oversize() -> OversizeOption:
        return OversizeOption(name="double", multiplier=2.0)


if __name__ == '__main__':
    unittest.main()
