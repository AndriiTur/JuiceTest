from pprint import pprint

from pages.home.home_page_methods import HomePage
from pages.login_form.login_form_methods import LoginForm
from utils.configs import Configuration


# def test_register_user_valid(home_page):
#     home_page: HomePage = home_page
#     login_page: LoginForm = home_page.open_form_for_login()
#
#     login_page.login_default_user()
#     is_displayed = home_page.is_user_logged_in()
#     assert is_displayed, "User logged in"
#
#
def test_login_valid(home_page):
    config_data = Configuration()
    pprint(config_data.config.run_options())
    home_page: HomePage = home_page
    login_page: LoginForm = home_page.open_form_for_login()

    login_page.login_default_user()
    is_displayed = home_page.is_user_logged_in()
    assert is_displayed, "User logged in"

# def test_my_function():
#     if not condition:
#         pytest.skip("Skipping test because condition is not met.")

# def test_login_upd(login_page):
#     logger.info('Start run test for Login2222222222222222')
#     page = login_page
#
#     page.login_default_user()
#     is_displayed = page.is_user_logged_in()
#     assert is_displayed, "login failed"
#
#
# def test_login_upd_2(login_page):
#     logger.info('Start run test for Login2222222222222222')
#     page = login_page
#
#     page.login_default_user()
#     is_displayed = page.is_user_logged_in()
#     assert is_displayed, "login failed"
#
#
# def test_login_upd_3(login_page):
#     logger.info('Start run test for Login33333333333333333')
#     page = login_page
#
#     page.login_default_user()
#     is_displayed = page.is_user_logged_in()
#     assert is_displayed, "login failed"
#
#
# def run_all_tests(login_page):
#     test_login_upd(login_page)
#     test_login_upd_2(login_page)
#     test_login_upd_3(login_page)
#
#
# if __name__ == '__main__':
#     run_all_tests()
