from __future__ import annotations

from .models import Todo


class TodoService:
    """In-memory teaching service; restarting the process clears data."""
    def __init__(self) -> None:
        self._next_id = 1
        self._todos: dict[int, Todo] = {}

    @staticmethod
    def validate_title(title: str) -> str:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        return title.strip()

    def create(self, title: str) -> Todo:
        title = self.validate_title(title)
        todo = Todo(id=self._next_id, title=title)
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def list(self) -> list[Todo]:
        return list(self._todos.values())

    def get(self, todo_id: int) -> Todo:
        return self._todos[todo_id]

    def update(self, todo_id: int, changes: dict) -> Todo:
        todo = self.get(todo_id)
        if not changes or set(changes) - {"title", "completed"}:
            raise ValueError("provide title and/or completed only")
        # Validate the entire patch before mutating anything.
        title = self.validate_title(changes["title"]) if "title" in changes else todo.title
        completed = changes.get("completed", todo.completed)
        if not isinstance(completed, bool):
            raise ValueError("completed must be a boolean")
        todo.title, todo.completed = title, completed
        return todo

    def complete(self, todo_id: int) -> Todo:
        return self.update(todo_id, {"completed": True})

    def delete(self, todo_id: int) -> None:
        self._todos.pop(todo_id)
