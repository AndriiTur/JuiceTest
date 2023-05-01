import datetime
from pprint import pprint

import pytest

from selenium import webdriver
from termcolor import colored
from _pytest.reports import BaseReport
from pages.home.home_page_methods import HomePage
from utils.configs import Configuration
from utils.drivers import get_driver


@pytest.fixture()
def driver(request):
    config = Configuration().config

    # Get the value of the command-line option '--browser'
    pprint("TESTTEST")
    # browser_name = request.config.getoption("--browser")
    browser_name = "chrome"

    # Get the value of the command-line option '--headless'
    # headless = request.config.getoption("--headless")
    headless = None

    driver = get_driver(browser_name)
    # Make sure the WebDriver instance is cleaned up properly
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver) -> HomePage:
    yield HomePage(driver)


def pytest_report_header(config):
    now = datetime.datetime.now()
    return colored(f"The tests run on {now:%Y-%m-%d %H:%M:%S}", "green")


def pytest_report_teststatus(report: BaseReport, config):
    """
    Override the default test status reporting behavior to include custom messages.

    This hook function is called for each test item and can be used to customize the
    reporting of test results.

    :param report: The test report object containing information about the test run.
    :param config: The pytest configuration object.
    :return: A tuple of (status, short_text, long_text) representing the test status
             and associated messages.
    """

    if report.when == "call":
        if report.passed:
            # Customize the message for a passing test
            return "passed", "✓", "PASSED"
        elif report.failed:
            # Customize the message for a failing test
            return "failed", "✗", "FAILED"
        elif report.skipped:
            # Customize the message for a skipped test
            return "skipped", "S", "SKIPPED"
    elif report.when == "setup":
        if report.skipped:
            # Customize the message for a skipped setup
            return "skipped", "S", "SKIPPED SETUP"
    elif report.when == "teardown":
        if report.skipped:
            # Customize the message for a skipped teardown
            return "skipped", "S", "SKIPPED TEARDOWN"
