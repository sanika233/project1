import pytest
from pages.login_page import LoginPage
from utilities.config import VALID_EMAIL, VALID_PASSWORD, INVALID_EMAIL, INVALID_PASSWORD


class TestLogin:

    # TC-6
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_EMAIL, VALID_PASSWORD)
        login_page.wait_for_login_success()
        assert login_page.is_displayed(login_page.PROFILE_ICON), \
            "User login failed or profile icon not displayed"

    # TC-7
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_EMAIL, INVALID_PASSWORD)
        assert "login" in driver.current_url.lower() or "sign-in" in driver.current_url.lower(), \
            "User was navigated away despite invalid credentials"

    # TC-10
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_EMAIL, VALID_PASSWORD)
        assert login_page.is_logout_visible(), \
            "Logout button is not visible"

        login_page.click_logout()
        login_page.dismiss_overlays()
        assert "login" in driver.current_url.lower() or "sign-in" in driver.current_url.lower() or "guvi" in driver.current_url.lower(), \
            "Logout navigation failed"