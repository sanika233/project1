from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.config import LOGIN_URL


class LoginPage(BasePage):
    # -----------------------------
    # Locators
    # -----------------------------

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (
        By.XPATH,
        "//button[@id='login-btn'] | "
        "//button[contains(text(), 'Login')] | "
        "//a[contains(text(), 'Login')] | "
        "//button[@type='submit']"
    )

    PROFILE_ICON = (
        By.XPATH,
        "//div[contains(@class, 'gravatar-wrap')] | "
        "//div[contains(@class, 'profile')] | "
        "//img[contains(@class, 'avatar') or contains(@alt, 'profile')] | "
        "//*[contains(@class, 'user-profile') or contains(@class, 'avatar')]"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//*[@id='signout'] | "
        "//p[normalize-space()='Sign Out'] | "
        "//*[contains(normalize-space(), 'Sign Out')] | "
        "//*[contains(normalize-space(), 'Signout')] | "
        "//*[contains(normalize-space(), 'Logout')]"
    )

    ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(@class, 'invalid-feedback') or contains(@class, 'error') or contains(@class, 'toast')]"
    )

    # -----------------------------
    # Page Actions
    # -----------------------------

    def open(self):
        self.navigate(LOGIN_URL)

    def dismiss_overlays(self):
        """Remove overlay elements like cookie consent banners that intercept clicks."""
        try:
            self.driver.execute_script(
                "var banner = document.getElementById('ccbar_container'); if (banner) banner.remove();"
            )
        except Exception:
            pass

    def enter_email(self, email):
        element = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    def click_login_submit(self):
        self.dismiss_overlays()
        try:
            self.click(self.LOGIN_SUBMIT_BUTTON)
        except Exception:
            element = self.driver.find_element(*self.LOGIN_SUBMIT_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_submit()

    def wait_for_login_success(self):
        self.dismiss_overlays()
        self.wait.until(EC.visibility_of_element_located(self.PROFILE_ICON))

    def open_profile_menu(self):
        self.wait_for_login_success()

        try:
            if self.driver.find_element(*self.LOGOUT_BUTTON).is_displayed():
                return
        except Exception:
            pass

        try:
            element = self.wait.until(EC.element_to_be_clickable(self.PROFILE_ICON))
            element.click()
        except Exception:
            element = self.driver.find_element(*self.PROFILE_ICON)
            self.driver.execute_script("arguments[0].click();", element)

    def is_logout_visible(self):
        self.open_profile_menu()
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON)).is_displayed()
        except Exception:
            return False

    def click_logout(self):
        self.dismiss_overlays()
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
            element.click()
        except Exception:
            element = self.driver.find_element(*self.LOGOUT_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)