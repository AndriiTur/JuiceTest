from typing import List

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_driver(browser_name="chrome", driver_options: List = ["--window-size=1200,800"]):
    # Create the WebDriver instance based on the chosen browser and its options
    options = None
    if browser_name == "chrome":
        if driver_options:
            options = webdriver.ChromeOptions()
            for option in driver_options:
                options.add_argument(option)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        if driver_options:
            options = webdriver.FirefoxOptions()
            for option in driver_options:
                options.add_argument(option)
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install, options=options)
    elif browser_name == "edge":
        if driver_options:
            options = webdriver.EdgeOptions()
            for option in driver_options:
                options.add_argument(option)
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
    elif browser_name == "chromium":
        if driver_options:
            options = webdriver.ChromeOptions()
            for option in driver_options:
                options.add_argument(option)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    else:
        raise ValueError(f"Invalid browser choice: {browser_name}")

    return driver
