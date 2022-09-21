from dataclasses import dataclass
from src.main.file_system import runfiles


@dataclass
class DashboardFormats:
    UPNEDIIMP: str = "//resources/forward_office/formats/upn_edi_imp.json"
