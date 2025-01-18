import datetime
import pytest
from playwright.sync_api import sync_playwright

URL = "https://todomvc.com/examples/react/dist/"


class TodoMVCPage:
    def __init__(self, page):
        self.page = page
        self.new_todo_input = page.locator(".new-todo")
        self.todo_list_items = page.locator(".todo-list li")

    def navigate(self):
        self.page.goto(URL)
        assert self.page.url == URL, "The URL is not correct"

    def add_todo(self, text):
        self.new_todo_input.fill(text)
        self.new_todo_input.press("Enter")

    def mark_todo_as_completed(self, text):
        todo_checkbox = self.page.locator(f".todo-list li:has-text('{text}') .toggle")
        todo_checkbox.click()

    def delete_todo(self, text):
        todo_item = self.page.locator(f".todo-list li:has-text('{text}')")
        todo_item.hover()
        todo_delete_button = todo_item.locator(".destroy")
        todo_delete_button.click()

    def is_todo_visible(self, text):
        return self.page.locator(f".todo-list li:has-text('{text}')").is_visible()

    def is_todo_completed(self, text):
        todo_item = self.page.locator(f".todo-list li:has-text('{text}')")
        return "completed" in todo_item.get_attribute("class")


def generate_todo_text(base_text, offset_days=0):
    date = datetime.date.today() + datetime.timedelta(days=offset_days)
    return f"{base_text} - {date}"


@pytest.fixture(scope="function")
def browser_context_with_video(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


def test_todomvc(browser_context_with_video):
    context = browser_context_with_video
    page = context.new_page()
    todo_page = TodoMVCPage(page)  # Initialize the page object

    todo_page.navigate()

    todo_1_text = generate_todo_text("TODO 1")
    todo_page.add_todo(todo_1_text)
    page.screenshot(path="screenshots/step2_add_todo1.png")
    assert todo_page.is_todo_visible(todo_1_text), "TODO 1 was not added"

    todo_2_text = generate_todo_text("TODO 2", offset_days=1)
    todo_page.add_todo(todo_2_text)
    page.screenshot(path="screenshots/step3_add_todo2.png")
    assert todo_page.is_todo_visible(todo_2_text), "TODO 2 was not added"

    todo_page.mark_todo_as_completed(todo_1_text)
    page.screenshot(path="screenshots/step4_complete_todo1.png")
    assert todo_page.is_todo_completed(todo_1_text), "TODO 1 was not marked as completed"

    todo_page.delete_todo(todo_2_text)
    page.screenshot(path="screenshots/step5_delete_todo2.png")
    assert not todo_page.is_todo_visible(todo_2_text), "TODO 2 was not deleted"
