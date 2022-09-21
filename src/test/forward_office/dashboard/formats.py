import unittest
from src.main.forward_office.dashboard.formats import DashboardFormats


class TestSystemPaths(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_can_get_dashboard_formats(self):
        formats = DashboardFormats()
        format = formats.UPNEDIIMP

        self.fail("Dummy fail for dashboard dataclass.")


if __name__ == '__main__':
    unittest.main()
