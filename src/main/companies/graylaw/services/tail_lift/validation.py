import re
from src.main.freight.consignment.interface import Consignment


class TailLiftValidationStrategy:
    def __init__(self, consignment: Consignment):
        self._consignment = consignment
        self._initialise_tail_lift_patterns()

    def _initialise_tail_lift_patterns(self):
        patterns = (
            "(tail lift|t/lift|t-lift|tail-lift|"
            "^tl( )+|( )+tl( )+|( )+tl$|^tl$|"
            "^t/l( )+|( )+t/l( )+|( )+t/l$|^t/l$)"
        )

        self._tail_lift_patterns = re.compile(patterns, flags=re.I)

    def has_tail_lift_error(self) -> bool:
        tail_lift_mentioned = False
        instructions = self._consignment.delivery_instructions

        for instruction in instructions:
            if re.search(self._tail_lift_patterns, instruction):
                tail_lift_mentioned = True

        return (
            tail_lift_mentioned
            and not self._consignment.service.tail_lift()
        )

    def has_dates_error(self) -> bool:
        dates = self._consignment.shipment_dates
        difference = dates.delivery_date - dates.collection_date

        if self._consignment.service.main().is_next_day():
            incongruent_delivery_date = difference != 1

        elif self._consignment.service.booked().is_booked():
            incongruent_delivery_date = difference < 2

        else:
            incongruent_delivery_date = difference != 2

        return incongruent_delivery_date
