import unittest
from src.main.upn.api.structures.data_types.primitives import UpnApiPrimitives


class TestUpnApiPrimitives(unittest.TestCase):
    def test_should_get_field_type_of_primitive(self):
        self.assertEqual(str, UpnApiPrimitives().get("string"))


if __name__ == '__main__':
    unittest.main()
