import unittest
from src.main.forward_office.dashboard.formats import DashboardFormats


class TestDashboardFormats(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_can_get_a_dashboard_format(self):
        formats = DashboardFormats()
        format = formats.UPNEDIIMP

        print(format)

        self.fail("Dummy fail for dashboard dataclass.")


if __name__ == '__main__':
    unittest.main()
