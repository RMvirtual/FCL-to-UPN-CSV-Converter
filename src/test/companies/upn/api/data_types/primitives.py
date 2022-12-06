import unittest
from src.main.companies.upn.api.data_types.primitives.implementation import Primitives


class TestUPNPrimitivesUnmarshalling(unittest.TestCase):
    def test_should_get_field_type_of_primitive(self):
        self.assertEqual(str, Primitives().get("string"))


if __name__ == '__main__':
    unittest.main()
