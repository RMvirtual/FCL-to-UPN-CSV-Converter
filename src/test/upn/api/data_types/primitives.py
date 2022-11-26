import unittest
from src.main.upn.api.data_types.primitives import UPNAPIPrimitives


class TestUPNPrimitivesUnmarshalling(unittest.TestCase):
    def test_should_get_field_type_of_primitive(self):
        self.assertEqual(str, UPNAPIPrimitives().get("string"))


if __name__ == '__main__':
    unittest.main()
