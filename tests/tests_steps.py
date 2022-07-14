import allure
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()
    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issue'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с заданым номером'):
        number_target = '#99'
        s(by.partial_text(number_target)).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    search_for_repository('76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')
    browser.wait_to(timeout=10)


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Open {repo}')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
