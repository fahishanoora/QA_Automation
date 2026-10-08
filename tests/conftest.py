import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--headless=new")  # Enable Headless Mode
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    # Store driver on request node so PyTest hooks can access it
    request.node.driver = driver
    
    yield driver
    driver.quit()

# Hook to capture screenshot on test failure and embed into HTML report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_b64 = driver.get_screenshot_as_base64()
            html = f'<div><img src="data:image/png;base64,{screenshot_b64}" style="width:600px;height:auto;" /></div>'
            extra.append(pytest_html.extras.html(html))
            report.extra = extra