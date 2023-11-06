import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser

import config
from wiki_app_test_project import utils


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    app_path = os.path.join(
        config.BASE_DIR,
        'wiki_app_test_project',
        'app',
        'app-alpha-universal-release.apk'
    )
    options = UiAutomator2Options()
    if config.settings.ENVIRONMENT == 'local':
        capabilities = {
            'platformName': 'Android',
            'platformVersion': '10.0',
            'automationName': 'UiAutomator2',
            'udid': 'emulator-5554',
            'app': app_path,
            'appWaitActivity': 'org.wikipedia.*'
        }
        options.load_capabilities(capabilities)

        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            options=options
        )
    browser.config.driver = driver
    browser.config.timeout = 10.0

    yield

    utils.attach.add_screenshot(browser)
    utils.attach.add_xml(browser)
    if config.settings.ENVIRONMENT == 'bstack':
        session_id = browser.driver.session_id

    browser.quit()

    if config.settings.ENVIRONMENT == 'bstack':
        utils.attach.attach_bstack_video(session_id)
