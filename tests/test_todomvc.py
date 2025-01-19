import allure
from helpers import generate_text_with_date


@allure.suite("TodoMVC Page")
class TestTodoMVCPage:
    def test_todomvc(self, todomvc_page):
        todo_1_text = generate_text_with_date("TODO 1")
        todomvc_page.add_todo(todo_1_text)
        todomvc_page.screenshot(path="screenshots/step1_add_todo1.png")
        assert todomvc_page.is_todo_visible(todo_1_text), "TODO 1 was not added"

        todo_2_text = generate_text_with_date("TODO 2", offset_days=1)
        todomvc_page.add_todo(todo_2_text)
        todomvc_page.screenshot(path="screenshots/step2_add_todo2.png")
        assert todomvc_page.is_todo_visible(todo_2_text), "TODO 2 was not added"

        todomvc_page.mark_todo_as_completed(todo_1_text)
        todomvc_page.screenshot(path="screenshots/step3_complete_todo1.png")
        assert todomvc_page.is_todo_completed(todo_1_text), "TODO 1 was not marked as completed"

        todomvc_page.delete_todo(todo_2_text)
        todomvc_page.screenshot(path="screenshots/step4_delete_todo2.png")
        assert not todomvc_page.is_todo_visible(todo_2_text), "TODO 2 was not deleted"
