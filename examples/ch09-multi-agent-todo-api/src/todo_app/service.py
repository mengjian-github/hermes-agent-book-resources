from __future__ import annotations

from .models import Todo


class TodoService:
    def __init__(self) -> None:
        self._next_id = 1
        self._todos: dict[int, Todo] = {}

    def create(self, title: str) -> Todo:
        title = title.strip()
        if not title:
            raise ValueError("title is required")
        todo = Todo(id=self._next_id, title=title)
        self._todos[todo.id] = todo
        self._next_id += 1
        return todo

    def list(self) -> list[Todo]:
        return list(self._todos.values())

    def complete(self, todo_id: int) -> Todo:
        todo = self._todos[todo_id]
        todo.completed = True
        return todo

    def delete(self, todo_id: int) -> None:
        self._todos.pop(todo_id)
