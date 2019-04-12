#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pytest
from .conftest import SPLUNK_INFO


@pytest.mark.parametrize('splunk_hec_handler', [
    [SPLUNK_INFO['host'], SPLUNK_INFO['hec_port'], SPLUNK_INFO['hec_token'], SPLUNK_INFO['index'],
     SPLUNK_INFO['source']],
    [SPLUNK_INFO['host'], SPLUNK_INFO['hec_port'], SPLUNK_INFO['hec_token'], SPLUNK_INFO['index'],
     None],
], indirect=True)
def test_handler_basic(splunk_hec_handler):
    """
    Checkpoint: 1. logs are sent to splunk 2. the default source field is datetime
    """
    logger = logging.getLogger(test_handler_basic.__name__ + str(id(splunk_hec_handler)))
    logger.addHandler(splunk_hec_handler)
    logger.setLevel(logging.INFO)
    logger.info('hello world!')


@pytest.mark.parametrize('splunk_hec_handler', [
    [SPLUNK_INFO['host'], SPLUNK_INFO['hec_port'], SPLUNK_INFO['hec_token'], SPLUNK_INFO['index'],
     SPLUNK_INFO['source']],
], indirect=True)
def test_log_in_multiprocess(splunk_hec_handler):
    """
    Checkpoint: 1. log sent to splunk
    """

    def _test():
        logger = logging.getLogger('sub_process')
        logger.addHandler(splunk_hec_handler)
        logger.setLevel(logging.INFO)
        logger.info('hello again!')

    from multiprocessing import Process
    p = Process(target=_test)
    p.start()
    p.join()


@pytest.mark.parametrize('splunk_hec_handler', [
    [SPLUNK_INFO['host'], SPLUNK_INFO['hec_port'], SPLUNK_INFO['hec_token'], SPLUNK_INFO['index'],
     SPLUNK_INFO['source']],
], indirect=True)
def test_log_exception(splunk_hec_handler):
    logger = logging.getLogger(test_log_exception.__name__)
    logger.addHandler(splunk_hec_handler)
    try:
        1 / 0
    except Exception as e:
        logger.error(e, exc_info=True)
