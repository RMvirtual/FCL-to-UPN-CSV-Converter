import unittest
from src.main.upn.api.interfaces.primitives import UPNAPIPrimitives


class TestUPNAPIPrimitivesInterface(unittest.TestCase):
    def test_should_get_field_type_of_primitive(self):
        self.assertEqual(str, UPNAPIPrimitives().get("string"))


if __name__ == '__main__':
    unittest.main()
