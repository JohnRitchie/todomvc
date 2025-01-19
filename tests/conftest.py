import pytest
import allure
from playwright.sync_api import sync_playwright
from pages.todomvc_page import TodoMVCPage


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Headless mode if supplied.")

@pytest.fixture(scope="session")
def browser_context_with_video(pytestconfig):
    headless = pytestconfig.getoption("--headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def todomvc_page(page):
    with allure.step("Creating a session"):
        page_obj = TodoMVCPage(page)
        page_obj.navigate()

    return page_obj
