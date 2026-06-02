from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from todo_app import TodoService


class TodoServiceTests(unittest.TestCase):
    def test_create_and_list_todos(self) -> None:
        service = TodoService()

        todo = service.create("Write tests")

        self.assertEqual(todo.id, 1)
        self.assertEqual(service.list(), [todo])

    def test_rejects_empty_title(self) -> None:
        service = TodoService()

        with self.assertRaises(ValueError):
            service.create("   ")

    def test_complete_todo(self) -> None:
        service = TodoService()
        todo = service.create("Review API")

        completed = service.complete(todo.id)

        self.assertTrue(completed.completed)

    def test_delete_todo(self) -> None:
        service = TodoService()
        todo = service.create("Remove me")

        service.delete(todo.id)

        self.assertEqual(service.list(), [])


if __name__ == "__main__":
    unittest.main()
