import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.label('owner', 'unknown')
    allure.dynamic.feature('Задачи в репощитории')
    allure.dynamic.story('неавторизованный пользователь не может создать задачу и репозиторий')
    allure.dynamic.link('https://gitcub.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'unknown')
@allure.feature('Задачи в репощитории')
@allure.story('Авторизованный пользователь может создать задачу и репозиторий')
@allure.link('https://gitcub.com', name='Testing')
def test_decorator_labels():
    pass
