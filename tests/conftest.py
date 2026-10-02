import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run Chrome in headless mode"
    )

# PyTest Hook: Capture Screenshot & Generate AI Root Cause Analysis (RCA) on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # 1. Capture Screenshot
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            driver.save_screenshot(screenshot_path)

            # 2. Extract Failure Details
            exception_type = str(call.excinfo.typename) if call.excinfo else "UnknownError"
            exception_msg = str(call.excinfo.value) if call.excinfo else ""

            # 3. Generate AI Root Cause Analysis
            ai_rca_summary = generate_ai_rca(exception_type, exception_msg, item.name)

            # 4. Format HTML Content for pytest-html v4+
            html_content = f"""
            <div style="margin-top: 10px; font-family: sans-serif;">
                <div style="background-color: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; padding: 12px; border-radius: 6px; margin-bottom: 10px;">
                    <strong>🤖 SmartQA AI Root Cause Analysis:</strong><br/>
                    {ai_rca_summary}
                </div>
                <div>
                    <strong>Failure Screenshot:</strong><br/>
                    <img src="{screenshot_path}" alt="Failure Screenshot" style="width:400px; border:1px solid #ccc; border-radius:4px;" onclick="window.open(this.src)"/>
                </div>
            </div>
            """
            
            # Compatible with pytest-html 4.x
            try:
                import pytest_html
                extras.append(pytest_html.extras.html(html_content))
            except AttributeError:
                # Fallback for alternative pytest-html versions
                extras.append({"name": "AI RCA & Screenshot", "format": "html", "content": html_content})

    report.extras = extras


def generate_ai_rca(error_type, error_msg, test_name):
    """Categorizes Selenium/PyTest exceptions and outputs dynamic remediation steps."""
    if "StaleElementReferenceException" in error_type:
        return (
            f"<strong>Issue:</strong> DOM updated or re-rendered while interacting with an element in <code>{test_name}</code>.<br/>"
            f"<strong>Suggested Fix:</strong> Re-locate the element immediately before the action or use explicit wait with <code>EC.staleness_of</code> or <code>EC.element_to_be_clickable</code>."
        )
    elif "TimeoutException" in error_type:
        return (
            f"<strong>Issue:</strong> Explicit wait timed out waiting for an element in <code>{test_name}</code>.<br/>"
            f"<strong>Suggested Fix:</strong> Verify element locator, increase timeout duration, or ensure page layout rendered properly."
        )
    elif "AssertionError" in error_type:
        return (
            f"<strong>Issue:</strong> Assertion check failed during test execution.<br/>"
            f"<strong>Suggested Fix:</strong> Check actual vs expected values in the stacktrace and review page state in screenshot."
        )
    else:
        return (
            f"<strong>Issue:</strong> Test crashed with <code>{error_type}</code>.<br/>"
            f"<strong>Suggested Fix:</strong> Review exception logs: <em>{error_msg[:150]}...</em>"
        )