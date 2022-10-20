import unittest
from src.main.file_system.dashboard_format_files import DashboardFormatFiles


class TestDashboardFormats(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_can_get_a_dashboard_format_file(self):
        format_files = DashboardFormatFiles()
        format_path = format_files.UPNEDIIMP

        self.assertEqual(
            "resources/forward_office/dashboard_formats/upn_edi_imp.json",
            format_path
        )


if __name__ == '__main__':
    unittest.main()
