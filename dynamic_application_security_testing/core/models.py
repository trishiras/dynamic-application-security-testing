from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, List, Any, Dict, Literal, Union
from dynamic_application_security_testing.support.enums import ZAPJobType


class Response(BaseModel):
    """
    Represents the response structure.
    """

    data: List[str] = Field(default_factory=list)
    success: bool = Field(default=False)
    message: Optional[str] = Field(default=None)
    status_code: int = Field(default=200)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    meta: Dict[str, Any] = Field(default_factory=dict)


class Context(BaseModel):
    name: str = Field(default="DAST Scan Report")
    urls: List[str]


class EnvParameters(BaseModel):
    failOnError: bool = Field(default=False)
    failOnWarning: bool = Field(default=False)
    progressToStdout: bool = Field(default=True)


class Env(BaseModel):
    contexts: List[Context]
    parameters: EnvParameters


class PassiveScanConfigParameters(BaseModel):
    maxAlertsPerRule: int = Field(default=10)
    scanOnlyInScope: bool = Field(default=True)
    maxBodySizeInBytesToScan: int = Field(default=0)


class SpiderParameters(BaseModel):
    context: str
    url: str
    maxDuration: int = Field(default=30)
    maxDepth: int = Field(default=5)
    maxChildren: int = Field(default=10)


class SpiderAjaxParameters(BaseModel):
    context: str
    url: str
    maxDuration: int = Field(default=30)
    maxCrawlDepth: int = Field(default=10)
    numberOfBrowsers: int = Field(default=2)


class PassiveScanWaitParameters(BaseModel):
    maxDuration: int = Field(default=30)


class ActiveScanParameters(BaseModel):
    context: str
    policy: str = Field(default="Default Policy")
    maxRuleDurationInMins: int = Field(default=5)
    maxScanDurationInMins: int = Field(default=60)


# [high-level-report, modern, risk-confidence-html, sarif-json, traditional-html, traditional-html-plus, traditional-json, traditional-json-plus, traditional-md, traditional-pdf, traditional-xml, traditional-xml-plus]
class ReportParameters(BaseModel):
    template: str = Field(default="traditional-json")
    reportDir: str = Field(default="/tmp/")
    reportFile: str
    reportTitle: str
    reportDescription: str


## It doesn't work for python < 3.10

# class Job(BaseModel):
#     type: Literal[
#         ZAPJobType.PASSIVE_SCAN_CONFIG.value,
#         ZAPJobType.PASSIVE_SCAN_WAIT.value,
#         ZAPJobType.SPIDER_AJAX.value,
#         ZAPJobType.ACTIVE_SCAN.value,
#         ZAPJobType.SPIDER.value,
#         ZAPJobType.REPORT.value,
#     ]
#     parameters: (
#         PassiveScanConfigParameters
#         | SpiderParameters
#         | SpiderAjaxParameters
#         | PassiveScanWaitParameters
#         | ActiveScanParameters
#         | ReportParameters
#     )


class Job(BaseModel):
    type: Literal[
        ZAPJobType.PASSIVE_SCAN_CONFIG.value,
        ZAPJobType.PASSIVE_SCAN_WAIT.value,
        ZAPJobType.SPIDER_AJAX.value,
        ZAPJobType.ACTIVE_SCAN.value,
        ZAPJobType.SPIDER.value,
        ZAPJobType.REPORT.value,
    ]
    parameters: Union[
        PassiveScanConfigParameters,
        SpiderParameters,
        SpiderAjaxParameters,
        PassiveScanWaitParameters,
        ActiveScanParameters,
        ReportParameters,
    ]


class ZAPConfig(BaseModel):
    env: Env
    jobs: List[Job]
