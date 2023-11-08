import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser, have


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем экран приветствия')
def test_welcome_screen():
    with allure.step('Проверяем что открылся экран приветствия'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/scrollView')
        ).should(be.visible)
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/imageViewCentered')
        ).should(be.visible)


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем главный экран')
def test_main_screen():
    with allure.step('Закрываем экран приветствия'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
        ).click()

    with allure.step('Проверяем элементы главного экрана'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')
        ).should(be.visible)
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
        ).should(be.visible)


@allure.label('owner', 'ponomarev-iv1986')
@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.title('Проверяем поиск и открытие статьи')
def test_search_in_wiki():
    with allure.step('Закрываем экран приветствия'):
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
        ).click()
    with allure.step('Ищем статью'):
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
        ).click()
        browser.element(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
        ).type('Bill Gates')
    with allure.step('Открываем статью'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).first.click()

    with allure.step('Проверяем, что открылась нужная статья'):
        browser.element(
            (AppiumBy.XPATH, '//android.webkit.WebView[@text="Bill Gates"]')
        ).should(be.visible)
        browser.element(
            (AppiumBy.XPATH, '//android.webkit.WebView[@text="Bill Gates"]')
        ).should(have.text('Bill Gates'))
