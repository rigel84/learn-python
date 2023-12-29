import logging
from learn_python.utils import configure_logging


test_logger = logging.getLogger('testing')


def pytest_runtest_logreport(report):
    configure_logging()
    # Check if the report is about a test case (not setup/teardown)
    if report.when == 'call':
        # Get the test outcome
        outcome = report.outcome
        # Get the test name
        test_name = report.nodeid
        # Log the test outcome
        test_logger.info('[%s] %s', outcome.upper(), test_name)


def pytest_configure(config):
    # we're using this instead of pytest_sessionstart because the later appears
    # to not be called before the first session?
    configure_logging()
    test_logger.info('[START] pytest')


def pytest_sessionfinish(session, exitstatus):
    from learn_python.register import do_report
    test_logger.info('[STOP] pytest')
    do_report()
