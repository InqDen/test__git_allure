import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
задание №3
'''


def test_decorator_steps():
    # open browser in page github.com
    open_main_page()
    # search
    search_for_repository('eroshenkoam/allure-example')
    # passing by coincidence
    go_to_repository('eroshenkoam/allure-example')
    # passing by issue
    open_issue_tab()
    # checking if the specified number exists
    search_for_repository('76')


# open browser in page github.com
@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')
    browser.wait_to(timeout=10)


# search
@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    # click search input
    s('.header-search-input').click()
    # enter data
    s('.header-search-input').send_keys(repo)
    # search
    s('.header-search-input').submit()


# passing by coincidence
@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


# passing by issue
@allure.step('Open {repo}')
def open_issue_tab():
    s('#issues-tab').click()


# checking if the specified number exists
@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
