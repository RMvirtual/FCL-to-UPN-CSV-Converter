import unittest
from src.main.upn.api.structures import primitives


class TestUpnApiPrimitives(unittest.TestCase):
    def test_should_get_field_type_of_primitive(self):
        self.assertEqual(str, primitives.get_primitive("string"))


if __name__ == '__main__':
    unittest.main()
