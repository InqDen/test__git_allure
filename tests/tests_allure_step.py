import allure
from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
задине №2
'''


def test_dynamic_steps():
    # open browser in page github.com
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        # click search input
        s('.header-search-input').click()
        # enter data
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        # search
        s('.header-search-input').submit()

    # passing by coincidence
    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    # passing by issue
    with allure.step('Открываем таб Issue'):
        s('#issues-tab').click()

    # checking if the specified number exists
    with allure.step('Проверяем наличие Issue с заданым номером'):
        number_target = '#99'
        s(by.partial_text(number_target)).should(be.visible)
