from src.main.freight.consignment.model import Consignment

from src.main.third_party_bridges.graylaw_forward_office.consignment_import\
    .parser.consignment import ConsignmentParser

from src.main.third_party_bridges.graylaw_forward_office.consignment_import\
    .parser.requests.factory import ParseRequestFactory

from src.main.third_party_bridges.graylaw_forward_office.consignment_import\
    .reports.reports import ConsignmentImportReport


class FCLImportController:
    def __init__(self, import_format):
        self._parser = ConsignmentParser()
        self._import_format = import_format
        self._requests = ParseRequestFactory(self._import_format)
        self._imported_consignments: dict[str, Consignment] = {}

    def import_consignments(
            self, consignments: list[list[str]]) -> ConsignmentImportReport:
        report = ConsignmentImportReport()

        for consignment in consignments:
            request = self._requests.consignment_request(consignment)
            new_consignment = self._parser.parse(request)

            self._imported_consignments[
                str(new_consignment.references.consignment)] = new_consignment

        report.consignments = self._imported_consignments

        return report
