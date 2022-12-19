import unittest
from src.main.companies.upn.database.consignment.network.constraints \
    import NetworkConsignmentConstraints


class TestNetworkConsignmentConstraints(unittest.TestCase):
    def setUp(self):
        self._constraints = NetworkConsignmentConstraints()

    def test_should_get_type_constraint(self) -> None:
        self.assertEqual("int", self._constraints.depot_no.type)

    def test_should_get_value_constraints(self) -> None:
        self.assertListEqual(
            ["P", "S", "I", "R"], self._constraints.main_service.values)


if __name__ == "__main__":
    unittest.main()
