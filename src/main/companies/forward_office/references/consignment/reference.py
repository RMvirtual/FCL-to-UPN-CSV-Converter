from src.main.companies.forward_office.references.consignment import interface

from src.main.companies.forward_office.references.consignment.validation \
    import FCLReferenceValidationStrategy


class FCLConsignmentReference(interface.FCLConsignmentReference):
    def __init__(self, reference: str):
        self._validation = FCLReferenceValidationStrategy()
        self._prefix = "GR"
        self.number = reference

    def __str__(self) -> str:
        return self._prefix + self._number

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def number(self) -> str:
        return self._number

    @number.setter
    def number(self, new_number: str) -> None:
        self._raise_exception_if_invalid(new_number)
        self._number = self._strip_prefix(new_number)

    def _strip_prefix(self, reference: str) -> str:
        prefix_index = 0 if self._validation.matches_numeric(reference) else 2

        return reference[prefix_index:]

    def _raise_exception_if_invalid(self, reference: str) -> None:
        self._raise_exception_if_type_invalid(reference)
        self._raise_exception_if_format_invalid(reference)

    def _raise_exception_if_format_invalid(self, reference: str) -> None:
        if not self._validation.is_valid_reference(reference):
            message = (
                reference + " is an invalid format. Consignment references "
                "should match the patterns of either GRddddddddd or ddddddddd."
            )

            raise ValueError(message)

    @staticmethod
    def _raise_exception_if_type_invalid(reference) -> None:
        if not type(reference) is str:
            raise TypeError("Incorrect parameter type for a reference.")
