# Тест на проверку соответствия локализации кнопки
def test_button_local(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Поиск и проверка текста на кнопке
    button_text_elt = browser.find_element_by_css_selector(".btn-add-to-basket")
    button_text = button_text_elt.text
    assert button_text == "Añadir al carrito", f"Текст не соответствует выбраному языку. Текст на кнопке: \"{button_text}\""
