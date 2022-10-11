from src.main.freight.shipment_dates.model import ShipmentDates


def parse(date: str) -> ShipmentDates:
    shipment_dates = ShipmentDates()
    shipment_dates.delivery_date = date

    return shipment_dates
