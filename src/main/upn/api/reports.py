import dataclasses
import datetime


@dataclasses.dataclass
class NetworkPallet:
    consignment_barcode_no: str
    type: str
    size: str
    barcode_no: str


@dataclasses.dataclass
class NetworkConsignment:
    con_no: str
    depot: int
    customer_reference: str
    despatch_date: datetime.datetime
    delivery_name: str
    delivery_address_1: str
    delivery_town: str
    delivery_county: str
    delivery_post_code: str
    delivery_telephone_no: str
    total_weight: int
    special_instructions: str
    customer_id: int
    delivery_contact_name: str
    delivery_country: str
    customer_paperwork_required: int
    main_service: str
    premium_service: str
    tail_lift: str
    extra_service: str
    delivery_date_time: datetime.datetime
    barcode_no: str
    pallets: list[NetworkPallet]
