from enum import Enum


class MixedTypeEnum(Enum):
    # Boolean constants
    SUCCESS = True

    # String constants
    OUTPUT = "output"
    TMP = "tmp"


class ZAPJobType(Enum):
    PASSIVE_SCAN_CONFIG = "passiveScan-config"
    SPIDER = "spider"
    SPIDER_AJAX = "spiderAjax"
    PASSIVE_SCAN_WAIT = "passiveScan-wait"
    ACTIVE_SCAN = "activeScan"
    REPORT = "report"


class ZAPReport(Enum):
    REPORT_NAME = "ZAP Report for {target}"
    REPORT_TITLE = "ZAP Scan Report of {target}"
    REPORT_DESCRIPTION = "This report contains the results of a comprehensive ZAP scan against the target application : {target}"


class ResponseMessage(Enum):
    ZAP_MSG = "ZAProxy did not return any response"


class STDInput(Enum):
    ZAP = "/zap/zap.sh -cmd -autorun {yaml_config_file}"
