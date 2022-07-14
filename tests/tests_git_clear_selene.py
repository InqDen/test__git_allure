from selene import be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

'''
задание №1
'''


def test_github():
    # open browser in page github.com
    browser.open('https://github.com')
    # click search input
    s('.header-search-input').click()
    # enter data
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    # search
    s('.header-search-input').submit()
    # passing by coincidence
    s(by.link_text('eroshenkoam/allure-example')).click()
    # passing by issue
    s('#issues-tab').click()
    # checking if the specified number exists
    s(by.partial_text('#80')).should(be.visible)
