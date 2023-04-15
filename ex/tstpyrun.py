import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1() -> None:
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


def test_exception2() -> None:
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self) -> None:
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self) -> None:
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self) -> None:
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self) -> None:
        self.browser.get(link)
        self.browser.find_element_by_css_selector(
            ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self) -> None:
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self) -> None:
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self) -> None:
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self) -> None:
        self.browser.get(link)
        self.browser.find_element_by_css_selector(
            ".basket-mini .btn-group > a")


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser) -> None:
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser) -> None:
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")


@pytest.fixture(scope='class')
def browser():
    driver = webdriver.Chrome()
    # Изменяем размер окна до 2000*1200 пикселей
    driver.set_window_size(2000, 1200)
    driver.get(link)
    driver.implicitly_wait(25)
    yield driver
    print('teardown')
    driver.quit()


@pytest.yield_fixture  # выполняется для каждой функции
def clean_cart(browser):
    yield  # по завершении теста выполняется код, который идет после этой команды
    print('yield')
    browser.get('https://*******.com/ru/cabinet/')  # Возвращаемся в ЛК
    # Открываем окно магазина
    time.sleep(5.0)  # ждём загрузки страницы
    store = browser.find_element_by_css_selector(
        '[data-test="widget__button-store"]')  # ищем кнопку "магазин"
    # Скроллим страницу до кнопки "магазин"
    browser.execute_script("return arguments[0].scrollIntoView(true);", store)
    store.click()
    # Проверяем, что магазин загружен (ищем раздел "Обзор")
    browser.find_element_by_css_selector(
        '[data-test="sidebar__button-REVIEW"]')
    try:
        remove = browser.find_elements_by_css_selector(
            '[data-test="cart__item-remove"]')  # Ищем все иконки удалить в корзине
        # Удаляем все товары из корзины
        for delete in remove:
            delete.click()  # Кликаем на каждую иокнку удалить
            time.sleep(1.0)
    except:
        pass
    finally:
        # Находим иконку "Закрыть" и кликаем на нее
        browser.find_element_by_css_selector(
            '[data-test="button-close"]').click()


def enter_on_start(browser):  # Логинимся
    browser.get(link)
    # Выполняем вход в аккаунт
    # ищем кнопку "Войти" и кликаем на неё
    browser.find_element_by_css_selector(
        '[data-template="#login_box"]').click()
    browser.login = browser.find_element_by_id('login_mail')
    browser.login.send_keys('*******@gmail.com')
    browser.password = browser.find_element_by_id('login_pass')
    browser.password.send_keys('*********')
    browser.find_element_by_id('agreementSocial').click()
    browser.find_element_by_id('login_submit').click()


def enter_on_pro_plus(browser):  # Логинимся в *******.com пользователь с ТП Про+
    browser.get(link)
    # Выполняем вход в аккаунт
    browser.find_element_by_css_selector(
        '[data-template="#login_box"]').click()  # ищем кнопку "Войти"
    browser.login = browser.find_element_by_id('login_mail')
    browser.login.send_keys('******_1@*******.com')
    browser.password = browser.find_element_by_id('login_pass')
    browser.password.send_keys('******')
    browser.find_element_by_id('agreementSocial').click()
    browser.find_element_by_id('login_submit').click()


def open_store(browser):  # Функция открывает магазин
    time.sleep(5.0)  # ждём загрузки страницы
    store = browser.find_element_by_css_selector(
        '[data-test="widget__button-store"]')  # ищем кнопку "магазин"
    # Скроллим страницу до кнопки "магазин"
    browser.execute_script("return arguments[0].scrollIntoView(true);", store)
    store.click()
    # Проверяем, что магазин загружен (ищем раздел "Обзор")
    browser.find_element_by_css_selector(
        '[data-test="sidebar__button-REVIEW"]')


def close_store(browser):  # Функция будет закрывать магазин
    # Находим иконку "Закрыть" и кликаем на нее
    browser.find_element_by_css_selector('[data-test="button-close"]').click()


def delete_all(browser):  # Функция отменяет оплату, удаляет все товары из корзины и закрывает магазин
    browser.get('https://*******.com/ru/cabinet/')  # Возвращаемся в ЛК
    open_store(browser)  # Открываем окно магазина
    browser.goods = browser.find_elements_by_css_selector(
        '[data-test="cart__item-remove"]')  # Ищем все иконки удалить в корзине
    # Удаляем все товары из корзины
    for browser.good in browser.goods:
        browser.good.click()  # Кликаем на каждую иокнку удалить
        time.sleep(1.0)
    close_store(browser)


def logout(browser) -> None:  # Функция осуществляет выход из аккаунта
    browser.avatar = browser.find_element_by_css_selector(
        '[data-test="widget__button-user"]')
    # Скроллим страницу так, чтобы был виден аватар профиля
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", browser.avatar)
    browser.avatar.click()  # клик на аватар профиля
    browser.escape = browser.find_element_by_xpath(
        '//button[contains(text(), "Выход")]')
    # Скроллим страницу так, чтобы была видна кнопка "Выйти"
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", browser.escape)
    time.sleep(2.0)
    browser.escape.click()  # Выходим из аккаунта
    time.sleep(2.0)


class TestGlobal():
    # Пользователь с ТП Старт/ПРО. Переход в вкладку "Виджет"
    def test_go_to_tab_vidget(self, browser) -> None:
        # здесь в функцию enter_on_start передаём имя фикстуры, в которой инициализирован браузер
        enter_on_start(browser)
        open_store(browser)
        browser.find_element_by_css_selector(
            '[data-test="sidebar__button-WIDGET"]').click()
        browser.find_element_by_css_selector(
            '[src="https://files.*******.com/upload/projects/images/*******/201710/thumb100x100_w_9db657467f8fe87796e1c7405a57824e_668f48d6.jpg"]')
        # Ищем кнопку "Перейти" и кликаем на нее
        browser.find_element_by_css_selector(
            '[data-test="widget__go-over"]').click()
        # Второй открытой вкладке (после клика на "Перейти" открывается новая вкладка) присваиваем имя "new_window"
        browser.new_window = browser.window_handles[1]
        browser.window = browser.window_handles[0]
        # Переходим на вторую вкладку
        browser.switch_to.window(browser.new_window)
        browser.find_element_by_class_name('header__Back-sc-1ws5ve8-2.ikSpXv')
        browser.close()
        browser.switch_to.window(browser.window)
        close_store(browser)

    # Корзина. Удалить товар
    def test_basket_delete_goods(self, browser, clean_cart):
        open_store(browser)
        browser.find_element_by_css_selector(
            '[data-test="sidebar__button-RENDERS"]').click()  # Переходим в раздел "Рендеры"
        # Добавляем пробный рендер в корзину
        browser.find_element_by_css_selector(
            '[data-test="card_products-0"] [data-test="card__button-in-cart"]').click()
        # Переходм в корзину с карточки "Пробный рендер"
        browser.find_element_by_css_selector(
            '[data-test="card_products-0"] [data-test="card__button-go-over"]').click()
        # Клик на иконку корзины (удаляем товар из корзины)
        browser.find_element_by_css_selector(
            '[data-test="cart__item-remove"]').click()
        close_store(browser)

    # Оплата товара банковской картой
    def test_payment_with_card(self, browser, clean_cart):
        open_store(browser)
        browser.find_element_by_css_selector(
            '[data-test="sidebar__button-RENDERS"]').click()  # Переходим в раздел "Рендеры"
        # Добавляем пробный рендер в корзину
        browser.find_element_by_css_selector(
            '[data-test="card_products-0"] [data-test="card__button-in-cart"]').click()
        # Переходм в корзину с карточки "Пробный рендер"
        browser.find_element_by_css_selector(
            '[data-test="card_products-0"] [data-test="card__button-go-over"]').click()
        # browser.find_element_by_css_selector('[data-test="cart__agreement"]').click() #Соглашаемся с условиями
        browser.find_element_by_css_selector('[for="agreement"]').click()
        browser.find_element_by_css_selector(
            '[data-test="cart__go-to-pay"]').click()  # Переходим к оплате
        browser.find_element_by_css_selector(
            '[aria-label="Google Pay"]')  # Ждем загрузки страницы оплаты
        delete_all(browser)
