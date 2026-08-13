import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """Add CLI argument to pass browser type."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser choice: chrome, firefox, or edge"
    )


@pytest.fixture
def driver(request):
    """Fixture to instantiate and tear down cross-browser drivers."""
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver_instance = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver_instance = webdriver.Edge(service=service)
    else:
        raise pytest.UsageError(
            f"Unsupported browser: '{browser_name}'. Choose from 'chrome', 'firefox', or 'edge'."
        )

    driver_instance.maximize_window()
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit()