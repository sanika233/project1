from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from utilities.config import BASE_URL


class HomePage(BasePage):

    # -----------------------------
    # Locators
    # -----------------------------

    LOGIN_BUTTON = (
        By.XPATH,
        "//a[@id='login-btn'] | "
        "//a[contains(@href, 'sign-in')] | "
        "//a[normalize-space()='Login'] | "
        "//button[normalize-space()='Login']"
    )

    SIGNUP_BUTTON = (
        By.XPATH,
        "//a[contains(@href, 'register') or contains(@href, 'sign-up') or normalize-space()='Sign up' or normalize-space()='Sign Up'] | "
        "//button[normalize-space()='Sign up' or normalize-space()='Sign Up']"
    )

    COURSES_MENU = (
        By.XPATH,
        "//p[contains(text(), 'Courses')] | "
        "//span[contains(text(), 'Courses')] | "
        "//a[contains(text(), 'Courses')] | "
        "//*[normalize-space()='Courses']"
    )

    LIVE_CLASSES_MENU = (
        By.XPATH,
        "//p[contains(text(), 'LIVE Classes')] | "
        "//span[contains(text(), 'LIVE Classes')] | "
        "//a[contains(text(), 'LIVE Classes')] | "
        "//*[contains(text(), 'LIVE Classes')]"
    )

    PRACTICE_MENU = (
        By.XPATH,
        "//p[contains(text(), 'Practice')] | "
        "//span[contains(text(), 'Practice')] | "
        "//a[contains(text(), 'Practice')] | "
        "//*[contains(text(), 'Practice')]"
    )

    DOBBY_ASSISTANT = (
        By.XPATH,
        "//*[@id='zs_fl_chat'] | "
        "//*[@id='zsiq_float'] | "
        "//*[@id='zsiq_chat_wrap'] | "
        "//div[@data-id='zsalesiq'] | "
        "//*[contains(@aria-label, 'Chat Widget')]"
    )

    # -----------------------------
    # Page Actions
    # -----------------------------

    def open(self):
        self.navigate(BASE_URL)

    def get_page_title(self):
        return self.get_title()

    def is_login_button_visible(self):
        return self.is_displayed(self.LOGIN_BUTTON)

    def click_login(self):
        try:
            self.click(self.LOGIN_BUTTON)
        except Exception:
            element = self.find_element(self.LOGIN_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

    def is_signup_button_visible(self):
        return self.is_displayed(self.SIGNUP_BUTTON)

    def click_signup(self):
        try:
            self.click(self.SIGNUP_BUTTON)
        except Exception:
            element = self.find_element(self.SIGNUP_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_courses_visible(self):
        return self.is_displayed(self.COURSES_MENU)

    def is_live_classes_visible(self):
        return self.is_displayed(self.LIVE_CLASSES_MENU)

    def is_practice_visible(self):
        return self.is_displayed(self.PRACTICE_MENU)

    def is_dobby_visible(self, timeout=15):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.DOBBY_ASSISTANT)
            ).is_displayed()
        except Exception:
            return False

    def verify_login_page(self):
        self.wait.until(
            lambda d: "sign-in" in d.current_url.lower() or "login" in d.current_url.lower()
        )

    def verify_register_page(self):
        self.wait.until(
            lambda d: any(term in d.current_url.lower() for term in ["register", "sign-up", "signup"])
        )