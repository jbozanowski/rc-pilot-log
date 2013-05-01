# -*- coding: utf-8 -*-

import logging

from django.conf import settings
from django.test.simple import DjangoTestSuiteRunner


log = logging.getLogger(__name__)


class CustomTestRunner(DjangoTestSuiteRunner):
    def __init__(self, *args, **kwargs):
        super(CustomTestRunner, self).__init__(*args, **kwargs)

    def build_suite(self, test_labels, *args, **kwargs):
        suite = super(CustomTestRunner, self).build_suite(test_labels, *args, **kwargs)
        if not test_labels and settings.TEST_APPS_TO_SKIP:
            to_test = []
            for test in suite:
                test_module = test.__class__.__module__
                if not any(map(lambda x: test_module.startswith(x),
                               settings.TEST_APPS_TO_SKIP)):
                    to_test.append(test)
            suite._tests = to_test
        return suite
    
