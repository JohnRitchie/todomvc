import allure
from assertpy import assert_that
from helpers import generate_text_with_date


@allure.suite("TodoMVC Page")
class TestTodoMVCPage:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Check the basic functionality of the todo list")
    def test_todomvc(self, todomvc_page):
        with allure.step("Add a TODO item with the current date"):
            todo_1_text = generate_text_with_date("TODO 1")
            todomvc_page.add_todo(todo_1_text)
            todomvc_page.screenshot(path="screenshots/step1_add_todo1.png")

        with allure.step("Verify that the new to-do item appears in the list"):
            assert_that(todomvc_page.is_todo_visible(todo_1_text)).is_true()

        with allure.step("Add a TODO item for tomorrow"):
            todo_2_text = generate_text_with_date("TODO 2", offset_days=1)
            todomvc_page.add_todo(todo_2_text)
            todomvc_page.screenshot(path="screenshots/step2_add_todo2.png")

        with allure.step("Verify that the new to-do item appears in the list"):
            assert_that(todomvc_page.is_todo_visible(todo_2_text)).is_true()

        with allure.step("Mark TODO 1 as completed"):
            todomvc_page.mark_todo_as_completed(todo_1_text)
            todomvc_page.screenshot(path="screenshots/step3_complete_todo1.png")

        with allure.step("Verify that the item is displayed as completed"):
            assert_that(todomvc_page.is_todo_completed(todo_1_text)).is_true()

        with allure.step("Delete TODO 2"):
            todomvc_page.delete_todo(todo_2_text)
            todomvc_page.screenshot(path="screenshots/step4_delete_todo2.png")

        with allure.step("Verify that the item is removed from the list."):
            assert_that(todomvc_page.is_todo_visible(todo_2_text)).is_false()
