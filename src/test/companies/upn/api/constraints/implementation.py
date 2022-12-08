import unittest
from src.main.companies.upn.api.constraints.implementation \
    import ItemConstraint


class TestItemConstraint(unittest.TestCase):
    def setUp(self):
        self._constraint = ItemConstraint(str, ["Hello", "World"])

    def test_should_get_type_from_item_constraint(self) -> None:
        self.assertEqual(str, self._constraint.type)

    def test_should_get_values_from_constraint(self) -> None:
        self.assertListEqual(["Hello", "World"], self._constraint.values)

    def test_should_raise_exception_with_heterogenous_values(self) -> None:
        with self.assertRaises(TypeError):
            _ = ItemConstraint(str, ["Hello", 5])


if __name__ == '__main__':
    unittest.main()
