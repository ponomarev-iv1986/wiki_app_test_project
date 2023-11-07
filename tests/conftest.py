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
        'tests',
        'resources',
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
    else:
        capabilities = {
            'platformName': 'android',
            'platformVersion': '10.0',
            'deviceName': 'Google Pixel 3',
            'app': 'bs://dd472bc10e6ccca8b77ca9164700eab79a87cb6a',
            'bstack:options': {
                'projectName': 'First Python project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack first_test',
                'userName': config.settings.BSTACK_USER,
                'accessKey': config.settings.BSTACK_ACCESS_KEY
            }
        }
        options.load_capabilities(capabilities)
        driver = webdriver.Remote(
            command_executor='http://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.driver = driver
    browser.config.timeout = 10.0

    yield

    utils.attach.add_screenshot(browser)
    utils.attach.add_xml(browser)

    session_id = browser.driver.session_id

    browser.quit()

    if config.settings.ENVIRONMENT == 'bstack':
        utils.attach.attach_bstack_video(session_id)
