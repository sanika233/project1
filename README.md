# Automation Testing of EdTech Platform Web Application

Automated end-to-end testing of the GUVI web application using Selenium WebDriver, Python, and Pytest with Page Object Model (POM) architecture.

## Cross-Browser Execution Commands

Run tests across target browsers via the `--browser` flag:

```bash
# Execute in Chrome (Default)
pytest --browser chrome --html=reports/chrome_report.html --self-contained-html

# Execute in Microsoft Edge
pytest --browser edge --html=reports/edge_report.html --self-contained-html

Markdown# Automated Cross-Browser Testing of EdTech Platform (GUVI)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-9.x-yellow.svg)](https://docs.pytest.org/)
[![Page Object Model](https://img.shields.io/badge/Architecture-Page%20Object%20Model-orange.svg)]()

This repository contains a robust, end-to-end automated testing framework for the [GUVI EdTech Platform](https://www.guvi.in). 
Built with **Python**, **Selenium WebDriver**, and **Pytest**, the project implements the **Page Object Model (POM)** 
design pattern and supports cross-browser test execution across **Google Chrome**, **Microsoft Edge**.

---

##  Architecture & Design

The project uses the **Page Object Model (POM)** architecture to ensure high maintainability, reusability, and clean separation of concerns:

```text
GUVI_Project1/

 pages/                  # Page Object Model Layer
  __init__.py
   base_page.py        # Generic Selenium wrappers (Waits, Clicks, Inputs)
   home_page.py        # Locators & Actions for GUVI Home Page
   login_page.py       # Locators & Actions for GUVI Login/Authentication Page

tests/                  # Test Suite Layer
   __init__.py
    test_home.py        # Test Cases TC-01, TC-02, TC-03, TC-04, TC-05, TC-08, TC-09
    test_login.py       # Test Cases TC-06, TC-07, TC-10

utilities/              # Helper Utilities
         __init__.py
        config.py           # Configuration loader (.env, URLs, Constants)

reports/                # HTML Test Reports output directory
screenshots/            # Test Failure Artifacts
.env                    # Environment Variables (Credentials - Excluded from Git)
gitignore              # Git Ignore Rules
conftest.py             # Pytest Fixtures & Cross-Browser Driver Factory
pytest.ini              # Pytest Configuration
requirements.txt        # Python Project Dependencies
 README.md               # Project Documentation

Features Cross-Browser Validation: Seamlessly run test suites across Chrome, Firefox, and Edge using a command-line parameter.
 Automated Driver Management: Integrates webdriver-manager for driver installation and updates without manual executable downloads. 
 Page Object Model (POM): Decouples test scripts from UI locators to simplify UI updates. 
 Robust Synchronization: Explicit waits (WebDriverWait) handle dynamic DOM elements, JS popups, and overlay banners smoothly.
  Rich HTML Reporting: Automatically generates standalone visual HTML reports for each test run using pytest-html. 
  Secure Credential Handling: Isolates sensitive user credentials using .env files via python-dotenv. Test Coverage MatrixTest Case IDDescriptionModule
  TC-01Verify Home Page URL validationtests/test_home.py
  TC-02Verify Home Page Page Titletests/test_home.py
  TC-03Verify Login Button visibility and clickabilitytests/test_home.py
  TC-04Verify Sign-Up Button visibility and clickabilitytests/test_home.py
  TC-05Verify Sign-Up Navigation flowtests/test_home.py
  TC-06Verify Successful Login with valid credentialstests/test_login.py
  TC-07Verify Login prevention with invalid credentialstests/test_login.py
  TC-08Verify Navigation Menu Items (Courses, LIVE Classes, Practice)tests/test_home.py
  TC-09Verify Dobby Assistant Widget visibility (xfail annotated for dynamic DOM)tests/test_home.py
  TC-10Verify User Logout functionalitytests/test_login.py 
  Prerequisites & Installation1. PrerequisitesPython 3.10+Web Browsers: Installed instances of Google Chrome, or Microsoft Edge.2. Clone Repository & Setup Virtual EnvironmentBash# Clone the repository
git clone [https://github.com/your-username/GUVI_Project1.git](https://github.com/your-username/GUVI_Project1.git)
cd GUVI_Project1

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Configure Environment VariablesCreate a .env file in the root directory:Code snippetGUVI_EMAIL=your_email@example.com
GUVI_PASSWORD=your_password

Execution & Usage1. Run Tests by BrowserBash# Run on Google Chrome (Default)
pytest --browser chrome

# Run on Microsoft Edge
pytest --browser edge
2. Run Specific Test Files or Test CasesBash# Execute only Home Page tests
pytest tests/test_home.py --browser chrome

# Execute only Login tests
pytest tests/test_login.py --browser chrome

# Execute a single test case
pytest tests/test_login.py -k "test_valid_login" --browser chrome
3. Generate HTML ReportsBash# Generate report for Chrome run
pytest --browser chrome --html=reports/chrome_report.html --self-contained-html


https://drive.google.com/drive/folders/1cR7Rs5ngoXy4gsFbnfScqIXByLAUoJ-P