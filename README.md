# Enterprise Hybrid QA Automation Framework

A production-ready, hybrid automated test framework built with Python, PyTest, Selenium WebDriver, Requests, and SQLite3. Demonstrates Page Object Model (POM) architecture, API testing, SQL backend validation, and automated HTML reporting.

---

## 🏗️ Framework Architecture & Features

- **UI Test Automation**: Built using Selenium WebDriver 4 and Page Object Model (POM) for clean locator separation and reusable interaction methods.
- **API Automation**: Full CRUD coverage (`GET`, `POST`, `PUT`, `DELETE`) using Python `requests` and JSON response assertions.
- **SQL Backend Validation**: Direct database query verification using `sqlite3` and `INNER JOIN` relational validation.
- **Data-Driven Testing**: Parametrized test execution via `@pytest.mark.parametrize`.
- **Reporting & Logging**: Centralized `pytest.ini` configuration, auto-generated HTML execution reports (`pytest-html`), automated screenshot capture on failures, and structured `logging`.

---

## 📁 Directory Structure

```text
QA_Automation/
├── pages/                  # Page Object Model classes (Locators & Page Actions)
│   ├── login_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Unified Test Suite
│   ├── conftest.py         # PyTest fixtures & screenshot hook
│   ├── test_login_pom.py   # UI Login Tests
│   ├── test_cart_pom.py    # UI Shopping Cart Tests
│   ├── test_api_demo.py    # API CRUD Tests
│   └── test_db_demo.py     # SQL Database Validation Tests
├── pytest.ini              # Central PyTest & Logging Configuration
├── requirements.txt        # Project Dependencies
└── report.html             # Automated Execution Report