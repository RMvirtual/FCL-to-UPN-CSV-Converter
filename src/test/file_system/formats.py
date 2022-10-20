import unittest
from src.main.file_system.file_contents import forward_office


class TestDashboardFormats(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_can_get_a_dashboard_format_file(self):
        format_path = forward_office.DashboardFormatFiles().UPNEDIIMP

        self.assertEqual(
            "resources/forward_office/dashboard_formats/upn_edi_imp.json",
            format_path
        )


if __name__ == '__main__':
    unittest.main()
