import allure
from assertpy import assert_that
from helpers import generate_text_with_date


@allure.suite("TodoMVC Page")
class TestTodoMVCPage:
    def test_todomvc(self, todomvc_page):
        todo_1_text = generate_text_with_date("TODO 1")
        todomvc_page.add_todo(todo_1_text)
        todomvc_page.screenshot(path="screenshots/step1_add_todo1.png")
        assert_that(todomvc_page.is_todo_visible(todo_1_text)).is_true()

        todo_2_text = generate_text_with_date("TODO 2", offset_days=1)
        todomvc_page.add_todo(todo_2_text)
        todomvc_page.screenshot(path="screenshots/step2_add_todo2.png")
        assert_that(todomvc_page.is_todo_visible(todo_2_text)).is_true()

        todomvc_page.mark_todo_as_completed(todo_1_text)
        todomvc_page.screenshot(path="screenshots/step3_complete_todo1.png")
        assert_that(todomvc_page.is_todo_completed(todo_1_text)).is_true()

        todomvc_page.delete_todo(todo_2_text)
        todomvc_page.screenshot(path="screenshots/step4_delete_todo2.png")
        assert_that(todomvc_page.is_todo_visible(todo_2_text)).is_false()
