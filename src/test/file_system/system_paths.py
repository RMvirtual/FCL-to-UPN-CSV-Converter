import unittest
from src.main.file_system import system_paths


class TestSystemPaths(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_fcl_dashboard_files_path_is_readable(self):
        path = system_paths.load_file("FCL_DASHBOARD_FORMATS")
        correct_path = "resources/forward_office/dashboard_format_files.json"

        self.assertEqual(correct_path, path)


if __name__ == '__main__':
    unittest.main()
