link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket_link_on_the_main_page(browser):
    browser.get(link)
    browser.find_element_by_css_selector("body.default:nth-child(2) div.container-fluid.page:nth-child(3) div.page_inner div.content:nth-child(3) article.product_page div.row:nth-child(1) div.col-sm-6.product_main:nth-child(2) form.add-to-basket:nth-child(6) > button.btn.btn-lg.btn-primary.btn-add-to-basket:nth-child(3)")
