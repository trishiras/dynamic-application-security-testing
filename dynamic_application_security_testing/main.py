import os
import json
from argparse import Namespace
from dynamic_application_security_testing.services import zap
from dynamic_application_security_testing.core.logger import logger
from dynamic_application_security_testing.core.input import parse_args
from dynamic_application_security_testing.support.enums import ZAPReport, MixedTypeEnum


class DynamicApplicationSecurityTesting(object):
    def __init__(
        self,
        arguments: Namespace,
    ):
        self.data = {}
        self.target = arguments.target
        self.output_via = arguments.output_via
        self.webhook = arguments.webhook
        self.output_file_path = arguments.output_file_path

    def run(self):

        logger.info(
            f"Started generating dynamic application security testing report for target :- {self.target}"
        )

        if self.webhook:
            logger.info(f"Webhook URL :- {self.webhook}")

        if self.output_file_path:
            logger.info(f"Output file path :- {self.output_file_path}")

        output_dir = os.path.join(
            os.getcwd(),
            MixedTypeEnum.OUTPUT.value,
        )
        tmp_dir = os.path.join(
            os.getcwd(),
            MixedTypeEnum.TMP.value,
        )
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

        report_name = ZAPReport.REPORT_NAME.value.format(target=self.target)
        report_title = ZAPReport.REPORT_TITLE.value.format(target=self.target)
        report_description = ZAPReport.REPORT_DESCRIPTION.value.format(
            target=self.target
        )

        zap_response = zap.run(
            url=self.target,
            report_name=report_name,
            report_title=report_title,
            report_description=report_description,
        )

        if zap_response.success:
            self.data = zap_response.data
        else:
            logger.error(zap_response.message)

        with open(self.output_file_path, "w") as fp:
            json.dump(self.data, fp, indent=4, default=str)

        logger.info(
            f"Finished generating dynamic application security testing report for target :- {self.target}"
        )


def main():

    arguments, unknown = parse_args()

    dynamic_application_security_testing = DynamicApplicationSecurityTesting(
        arguments=arguments
    )
    dynamic_application_security_testing.run()
