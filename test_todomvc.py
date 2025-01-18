import datetime
import pytest
from playwright.sync_api import sync_playwright

URL = "https://todomvc.com/examples/react/dist/"

@pytest.fixture(scope="function")
def browser_context_with_video(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()

def generate_todo_text(base_text, offset_days=0):
    date = datetime.date.today() + datetime.timedelta(days=offset_days)
    return f"{base_text} - {date}"

# @pytest.mark.allure_label("suite", "TodoMVC Tests")
def test_todomvc(browser_context_with_video):
    context = browser_context_with_video
    page = context.new_page()

    page.goto(URL)
    assert page.url == URL, "The URL is not correct"

    todo_1_text = generate_todo_text("TODO 1")
    page.locator(".new-todo").fill(todo_1_text)
    page.locator(".new-todo").press("Enter")
    page.screenshot(path="screenshots/step2_add_todo1.png")
    assert page.locator(f".todo-list li:has-text('{todo_1_text}')").is_visible(), "TODO 1 was not added"

    todo_2_text = generate_todo_text("TODO 2", offset_days=1)
    page.locator(".new-todo").fill(todo_2_text)
    page.locator(".new-todo").press("Enter")
    page.screenshot(path="screenshots/step3_add_todo2.png")
    assert page.locator(f".todo-list li:has-text('{todo_2_text}')").is_visible(), "TODO 2 was not added"

    todo_1_checkbox = page.locator(f".todo-list li:has-text('{todo_1_text}') .toggle")
    todo_1_checkbox.click()
    page.screenshot(path="screenshots/step4_complete_todo1.png")
    assert "completed" in page.locator(f".todo-list li:has-text('{todo_1_text}')").get_attribute("class"), \
        "TODO 1 was not marked as completed"

    todo_2_delete_button = page.locator(f".todo-list li:has-text('{todo_2_text}') .destroy")
    page.locator(f".todo-list li:has-text('{todo_2_text}')").hover()
    todo_2_delete_button.click()
    page.screenshot(path="screenshots/step5_delete_todo2.png")
    assert not page.locator(f".todo-list li:has-text('{todo_2_text}')").is_visible(), "TODO 2 was not deleted"
