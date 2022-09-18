import src.main.forward_office.dashboard.fields.upn_edi_imp as \
    upn_edi_fcl_fields
import src.main.forward_office.dashboard.export.file_formats.csv as csv_reader


def import_upn_edi_imp_csv_fcl_export(csv_path: str):
    fields = upn_edi_fcl_fields.upn_edi_imp_format()

    stuff = csv_reader.read(
        csv_path=csv_path,
        field_indexes=fields,
        ignore_headers=True
    )

    return stuff
