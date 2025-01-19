from playwright.sync_api import Page
from assertpy import assert_that


class TodoMVCPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://todomvc.com/examples/react/dist/"
        self.new_todo_input = page.locator(".new-todo")

    def navigate(self):
        self.page.goto(self.url)
        assert_that(self.page.url).is_equal_to(self.url)

    def screenshot(self, path):
        self.page.screenshot(path=path)

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
