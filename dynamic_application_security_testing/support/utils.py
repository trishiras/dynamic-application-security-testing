import yaml
from dynamic_application_security_testing.core.logger import logger
from dynamic_application_security_testing.support.enums import ZAPJobType
from dynamic_application_security_testing.core.models import (
    Env,
    Job,
    Context,
    ZAPConfig,
    EnvParameters,
    SpiderParameters,
    ReportParameters,
    ActiveScanParameters,
    SpiderAjaxParameters,
    PassiveScanWaitParameters,
    PassiveScanConfigParameters,
)


def get_zap_config(
    url: str,
    report_name: str,
    report_dir: str,
    report_file: str,
    report_title: str,
    report_description: str,
    config_file: str,
) -> ZAPConfig:
    logger.info("Getting ZAP config")

    logger.info(
        f"Inputs url: {url}, report_name: {report_name}, report_file: {report_file}, report_title: {report_title}, report_description: {report_description}"
    )

    context = Context(
        urls=[url],
    )
    context.name = report_name

    env_parameters = EnvParameters()
    env_parameters.failOnError = True
    env_parameters.failOnWarning = False
    env_parameters.progressToStdout = True

    env = Env(
        contexts=[context],
        parameters=env_parameters,
    )

    spider_parameters = SpiderParameters(
        context=report_name,
        url=url,
    )
    spider_parameters.maxDuration = 30
    spider_parameters.maxDepth = 5
    spider_parameters.maxChildren = 10

    spider_ajax_parameters = SpiderAjaxParameters(
        context=report_name,
        url=url,
    )
    spider_ajax_parameters.maxDuration = 30
    spider_ajax_parameters.maxCrawlDepth = 10
    spider_ajax_parameters.numberOfBrowsers = 2

    passive_scan_config_parameters = PassiveScanConfigParameters()
    passive_scan_config_parameters.maxAlertsPerRule = 10
    passive_scan_config_parameters.scanOnlyInScope = True
    passive_scan_config_parameters.maxBodySizeInBytesToScan = 0

    passive_scan_wait_parameters = PassiveScanWaitParameters()
    passive_scan_wait_parameters.maxDuration = 30

    active_scan_parameters = ActiveScanParameters(
        context=report_name,
    )
    active_scan_parameters.maxRuleDurationInMins = 5
    active_scan_parameters.maxScanDurationInMins = 60

    report_parameters = ReportParameters(
        reportDir=report_dir,
        reportFile=report_file,
        reportTitle=report_title,
        reportDescription=report_description,
    )

    jobs = [
        Job(
            type=ZAPJobType.SPIDER.value,
            parameters=spider_parameters,
        ),
        Job(
            type=ZAPJobType.SPIDER_AJAX.value,
            parameters=spider_ajax_parameters,
        ),
        Job(
            type=ZAPJobType.PASSIVE_SCAN_WAIT.value,
            parameters=passive_scan_wait_parameters,
        ),
        Job(
            type=ZAPJobType.PASSIVE_SCAN_CONFIG.value,
            parameters=passive_scan_config_parameters,
        ),
        Job(
            type=ZAPJobType.ACTIVE_SCAN.value,
            parameters=active_scan_parameters,
        ),
        Job(
            type=ZAPJobType.REPORT.value,
            parameters=report_parameters,
        ),
    ]

    zap_config = ZAPConfig(
        env=env,
        jobs=jobs,
    )

    logger.info("ZAP config set up successfully")
    logger.info("ZAP config: %s", zap_config.dict())

    with open(config_file, "w") as file:
        yaml.dump(
            zap_config.dict(),
            file,
            default_flow_style=False,
        )

    logger.info(f"ZAP config saved successfully at : {config_file}")
