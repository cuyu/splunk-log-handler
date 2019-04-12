#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from splunk_log_handler import SplunkUdpHandler
from .conftest import SPLUNK_INFO


def test_handler_basic():
    logger = logging.getLogger(test_handler_basic.__name__)
    handler = SplunkUdpHandler(SPLUNK_INFO['host'], SPLUNK_INFO['udp_port'])
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info('hello from udp channel')


def test_log_exception():
    logger = logging.getLogger(test_log_exception.__name__)
    handler = SplunkUdpHandler(SPLUNK_INFO['host'], SPLUNK_INFO['udp_port'])
    logger.addHandler(handler)
    try:
        1 / 0
    except Exception as e:
        logger.error(e, exc_info=True)
