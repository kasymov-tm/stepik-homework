import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)

    time.sleep(10)

    button = browser.find_elements_by_css_selector("button[type='submit'].btn-add-to-basket")
    assert button, "Кнопка корзины не найдена"