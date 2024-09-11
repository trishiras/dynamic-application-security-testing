import os
import json
import uuid
import traceback
from dynamic_application_security_testing.core.logger import logger
from dynamic_application_security_testing.core.models import Response
from dynamic_application_security_testing.support.utils import get_zap_config
from dynamic_application_security_testing.support.enums import (
    STDInput,
    MixedTypeEnum,
    ResponseMessage,
)


def run(
    url: str,
    report_name: str,
    report_title: str,
    report_description: str,
) -> Response:
    resp = Response()
    data = None
    file_dir = os.path.join(
        os.getcwd(),
        MixedTypeEnum.TMP.value,
    )

    file_name = str(f"{uuid.uuid4()}.json")
    file = os.path.join(
        file_dir,
        file_name,
    )
    yaml_config_file = os.path.join(
        os.getcwd(),
        MixedTypeEnum.TMP.value,
        str(f"{uuid.uuid4()}.yaml"),
    )
    try:
        get_zap_config(
            url=url,
            report_name=report_name,
            report_dir=file_dir,
            report_file=file_name,
            report_title=report_title,
            report_description=report_description,
            config_file=yaml_config_file,
        )

        os.system(
            STDInput.ZAP.value.format(
                yaml_config_file=yaml_config_file,
            )
        )

        with open(file, "r") as fp:
            data = json.load(fp, strict=False)
        if data:
            resp.success = MixedTypeEnum.SUCCESS.value
            resp.data = data
    except Exception as err:
        resp.message = ResponseMessage.ZAP_MSG.value
        logger.error(err)
        logger.debug(traceback.format_exc())

    return resp
