from dataclasses import asdict

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from .service import TodoService


def create_app() -> Flask:
    app = Flask(__name__)
    service = TodoService()
    app.extensions["todo_service"] = service

    def object_body():
        body = request.get_json()  # 415 for a non-JSON request; 400 for malformed JSON.
        if not isinstance(body, dict):
            raise ValueError("request body must be a JSON object")
        return body

    @app.errorhandler(ValueError)
    def invalid(error):
        return jsonify(error=str(error)), 400

    @app.errorhandler(KeyError)
    def missing(error):
        return jsonify(error="todo not found"), 404

    @app.errorhandler(HTTPException)
    def http_error(error):
        return jsonify(error=error.description), error.code

    @app.get("/todos")
    def list_todos():
        return jsonify([asdict(todo) for todo in service.list()])

    @app.post("/todos")
    def create_todo():
        body = object_body()
        if set(body) != {"title"}:
            raise ValueError("provide title only")
        todo = service.create(body["title"])
        return jsonify(asdict(todo)), 201, {"Location": f"/todos/{todo.id}"}

    @app.get("/todos/<int:todo_id>")
    def get_todo(todo_id):
        return jsonify(asdict(service.get(todo_id)))

    @app.patch("/todos/<int:todo_id>")
    def update_todo(todo_id):
        return jsonify(asdict(service.update(todo_id, object_body())))

    @app.delete("/todos/<int:todo_id>")
    def delete_todo(todo_id):
        service.delete(todo_id)
        return "", 204

    return app
