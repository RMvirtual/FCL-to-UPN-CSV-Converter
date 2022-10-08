from src.main.freight.dates.model import ShipmentDates, Date


def parse(date: str) -> ShipmentDates:
    shipment_dates = ShipmentDates()
    shipment_dates.delivery_date = Date(date)

    return shipment_dates
