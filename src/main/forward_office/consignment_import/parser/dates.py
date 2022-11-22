from src.main.graylaw.shipment_dates.implementation import ShipmentDates


def parse(date: str) -> ShipmentDates:
    shipment_dates = ShipmentDates()
    shipment_dates.delivery_date = date

    return shipment_dates
