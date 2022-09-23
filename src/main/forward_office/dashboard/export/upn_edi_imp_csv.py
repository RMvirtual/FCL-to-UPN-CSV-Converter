from src.main.forward_office.dashboard import formats
from src.main.forward_office.dashboard.export.file_formats import csv


def import_upn_edi_imp_csv_fcl_export(csv_path: str):
    read_parameters = csv.ReadParameters()

    read_parameters.csv_path = csv_path
    read_parameters.ignore_headers = True
    read_parameters.field_indexes = formats.DashboardFormats().UPNEDIIMP

    return csv.read(read_parameters)
