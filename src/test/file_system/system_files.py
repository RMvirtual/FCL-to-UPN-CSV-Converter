import unittest
from src.main.file_system.file_readers import system_files


class TestSystemPaths(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fcl_dashboard_files_path_is_readable(self):
        path = system_files.load_path("FCL_DASHBOARD_FORMATS")

        correct_path = (
            "resources/forward_office/dashboard_formats/short_codes.json")

        self.assertEqual(correct_path, path)


if __name__ == '__main__':
    unittest.main()
