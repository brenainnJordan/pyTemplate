import os
import sys
import json
import unittest
import logging

from brenlib.utils import blLoggingUtils

# ** change these as appropriate **
ROOT_DIR_KEY = "BREN_PY_LIB_ROOT_DIR"
PROJECT_NAME = "pyTemplate"

# **

REJECT_ARGV_APPS = [
    "maya.exe"
]


def get_root_dir():
    """Get the root directory for ALL our python libraries
    (ie the folder where our repos are kept)
    This should be set as an environment variable as defined by ROOT_DIR_KEY
    """

    if ROOT_DIR_KEY not in os.environ:
        raise Exception("{} environment variable not found".format(ROOT_DIR_KEY))

    root_dir = os.environ[ROOT_DIR_KEY]
    root_dir = os.path.normpath(root_dir)

    if not os.path.exists(root_dir):
        raise Exception("root dir not found: {}".format(root_dir))

    return root_dir


ROOT_DIR = get_root_dir()

ROOT_DATA_DUMP_DIR = os.path.join(ROOT_DIR, "dataDump")
DATA_DUMP_DIR = os.path.join(ROOT_DATA_DUMP_DIR, PROJECT_NAME)


def get_basic_logger(name):
    logger = logging.getLogger(name)

    if not len(logger.handlers):
        handler = logging.StreamHandler()
        logger.addHandler(handler)

        formatter = logging.Formatter('%(levelname)s: %(message)s ~ %(name)s')
        logger.handlers[0].setFormatter(formatter)

        logger.propagate = False
        logger.setLevel(logging.INFO)

    return logger


class TestCase(unittest.TestCase):
    """Test case base class, with basic logging
    """

    USE_LOGGER = False

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)

        if self.USE_LOGGER:
            self._log = get_basic_logger(self.__class__.__name__)
            self.log.setLevel(logging.INFO)
        else:
            self._log = None

    @property
    def log(self):
        return self._log

    def log_info(self, msg):
        if self.log:
            self.log.info(msg)
        else:
            print("[ INFO ] {}".format(msg))

    def log_error(self, err):
        self.log_info(
            "Error caught: {}({})".format(type(err).__name__, err)
        )

        return True

    def log_dict(self, data):
        str_data = json.dumps(data, indent=4, sort_keys=True)
        self.log_info(str_data)

    def validate_result(self, result, expected_result, suffix=None):
        if result == expected_result:
            msg = "result valid: {}".format(result)
            if suffix:
                msg += suffix
            self.log_info(msg)
            return True
        else:
            msg = "Unexpected result: {} (expected result: {})".format(result, expected_result)
            if suffix:
                msg += suffix
            raise Exception(msg)

    def runTest(self):
        # stub method to allow instancing
        pass

    def test(self):
        # do the test
        return None
