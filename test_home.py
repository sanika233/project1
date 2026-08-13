import pytest
from pages.home_page import HomePage


class TestHomePage:

    # TC-1
    def test_verify_homepage_url(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert "guvi.in" in driver.current_url.lower(), \
            "GUVI homepage URL is not valid"

    # TC-2
    def test_verify_homepage_title(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        actual_title = home_page.get_page_title()
        assert "GUVI" in actual_title and "Learn to code" in actual_title, \
            f"Homepage title '{actual_title}' does not match expected title format"

    # TC-3
    def test_login_button_visible_and_clickable(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.is_login_button_visible(), \
            "Login button is not visible"

        home_page.click_login()
        home_page.verify_login_page()
        assert "sign-in" in driver.current_url.lower() or "login" in driver.current_url.lower(), \
            "User was not navigated to login page"

    # TC-4
    def test_signup_button_visible_and_clickable(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.is_signup_button_visible(), \
            "Sign-Up button is not visible"

        home_page.click_signup()
        home_page.verify_register_page()
        assert any(term in driver.current_url.lower() for term in ["register", "sign-up", "signup"]), \
            "User was not navigated to registration page"

    # TC-5
    def test_signup_navigation(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.click_signup()
        home_page.verify_register_page()
        assert any(term in driver.current_url.lower() for term in ["register", "sign-up", "signup"]), \
            "Signup navigation failed"

    # TC-8
    def test_navigation_menu_items(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.is_courses_visible(), \
            "Courses menu is not visible"
        assert home_page.is_live_classes_visible(), \
            "LIVE Classes menu is not visible"
        assert home_page.is_practice_visible(), \
            "Practice menu is not visible"

    # TC-9
    @pytest.mark.xfail(
        reason="Dobby widget can load dynamically and its DOM locator may change."
    )
    def test_dobby_assistant_visible(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        assert home_page.is_dobby_visible(), \
            "Dobby Assistant is not visible"