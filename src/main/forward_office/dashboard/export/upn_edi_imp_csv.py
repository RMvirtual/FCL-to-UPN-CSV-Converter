from src.main.forward_office.dashboard.fields.upn_edi_imp \
    import upn_edi_imp_format

from src.main.forward_office.dashboard.export.file_formats import csv


def import_upn_edi_imp_csv_fcl_export(csv_path: str):
    fields = upn_edi_imp_format()

    return csv.read(
        csv_path=csv_path,
        field_indexes=fields,
        ignore_headers=True
    )
