import unittest
from src.main.companies.upn.model.database.services.services import (
    UPNServicesDatabase, ServiceProvider)


class TestUPNServicesDatabase(unittest.TestCase):
    def setUp(self):
        self._database = UPNServicesDatabase()

    def test_should_get_all_services(self) -> None:
        result = self._database.all_services()
        self._assert_is_main_service(result.main_service)
        self._assert_is_premium_service(result.premium_service)
        self._assert_is_tail_lift_service(result.tail_lift_required)
        self._assert_is_additional_service(result.additional_service)

    def test_should_load_main_service(self) -> None:
        self._assert_is_main_service(self._database.main_service())

    def test_should_load_premium_service(self) -> None:
        self._assert_is_premium_service(self._database.premium_service())

    def test_should_load_tail_lift_service(self) -> None:
        self._assert_is_tail_lift_service(self._database.tail_lift_required())

    def test_should_load_additional_service(self) -> None:
        self._assert_is_additional_service(self._database.additional_service())

    def _assert_is_main_service(self, service: ServiceProvider) -> None:
        self._assert_service_has_values(
            service=service, constraints=["P", "S", "I", "R"], default="P")

    def _assert_is_premium_service(self, service: ServiceProvider) -> None:
        self._assert_service_has_values(
            service=service,
            constraints=["", "B10", "AM", "Timed", "Sat"], default=""
        )

    def _assert_is_tail_lift_service(self, service: ServiceProvider) -> None:
        self._assert_service_has_values(
            service=service, constraints=["", "TLift"], default="")

    def _assert_is_additional_service(self, service: ServiceProvider) -> None:
        self._assert_service_has_values(
            service=service, constraints=["", "BI", "Bkd", "OOH"], default="")

    def _assert_service_has_values(
            self, service: ServiceProvider, constraints: list[str], default: str
    ) -> None:
        self.assertListEqual(constraints, service.constraints())
        self.assertEqual(default, service.selection)


if __name__ == '__main__':
    unittest.main()
