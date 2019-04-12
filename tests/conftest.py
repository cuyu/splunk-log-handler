#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from splunk_log_handler import SplunkStreamHandler, SplunkHecHandler
from splunk_log_handler import consts
import time

SPLUNK_INFO = {
    'splunk_uri': 'https://localhost:8089',
    'host': 'localhost',
    'username': 'admin',
    'password': 'changed',
    'index': 'main',
    'source': 'testing',
    'tcp_port': 9997,
    'udp_port': 9984,
    'hec_port': 8088,
    'hec_token': '2bd4761d-49a1-4864-ae8a-fb3bb562775e',
}


@pytest.fixture(scope='function')
def splunk_stream_handler(request):
    handler = SplunkStreamHandler(*request.param)
    yield handler
    # Wait for logs sending to splunk
    time.sleep(2)
    consts._KEEP_STREAM_THREAD = False
    handler._thread.join()
    consts._KEEP_STREAM_THREAD = True
    consts.INIT_PROCESS = False
    consts.LOGGER.handlers = []
    del handler


@pytest.fixture(scope='function')
def splunk_hec_handler(request):
    host, port, token, index, source = request.param
    handler = SplunkHecHandler('https://{}:{}'.format(host, str(port)), token, index, source)
    yield handler
    # Wait for logs sending to splunk
    time.sleep(2)
    consts._KEEP_STREAM_THREAD = False
    handler._thread.join()
    consts._KEEP_STREAM_THREAD = True
    consts.INIT_PROCESS = False
    consts.LOGGER.handlers = []
    del handler
