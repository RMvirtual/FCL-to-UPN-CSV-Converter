import dataclasses


@dataclasses.dataclass
class Services:
    main_service: str = ""
    premium_service: str = ""
    tail_lift_required: str = ""
    additional_service: str = ""
